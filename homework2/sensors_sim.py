from random import random
from sys import argv

class Sensor:
    def __init__(self, sensor_id: int, hw_revision: str):
        self.sensor_id = sensor_id
        self.hw_revision = hw_revision

    def read_data(self):
        return {'sensor_id': self.sensor_id, 'hw_revision': self.hw_revision}
    
class WiredSensor(Sensor):
    def __init__(self, sensor_id: int, hw_revision: str):
        super().__init__(sensor_id, hw_revision)

    def read_data(self):
        data = super().read_data()
        
        data['checksum'] = self.calculate_checksum(data)
        return data

    def calculate_checksum(self, data: dict) -> str:
        if random() < 0.01:
            return 'corrupted'
        return str(sum(ord(c) for c in str(data)) % 256)
    
class WirelessSensor(Sensor):
    def __init__(self, sensor_id: int, hw_revision: str, loss_probability: float):
        super().__init__(sensor_id, hw_revision)
        self.loss_probability = loss_probability

    def read_data(self):
        if random() < self.loss_probability:
            return None
        return super().read_data()

class GPSSensor(WiredSensor):
    def __init__(self, sensor_id: int, hw_revision: str, x: float = 0.0, y: float = 0.0):
        super().__init__(sensor_id, hw_revision)
        self.x = x
        self.y = y

    def read_data(self):
        return {'x': self.x, 'y': self.y}

class SteeringSensor(WiredSensor):
    def __init__(self, sensor_id: int, hw_revision: str):
        super().__init__(sensor_id, hw_revision)
        self.angle = 0.0
        self.speed = 0.0

    def read_data(self):
        self.angle += 1.0
        self.speed += 0.5
        return {'angle': self.angle, 'speed': self.speed}

class TemperatureSensor(WirelessSensor):
    def __init__(self, sensor_id: int, hw_revision: str, loss_probability: float):
        super().__init__(sensor_id, hw_revision, loss_probability)
        self.internal_temp = 20.0
        self.external_temp = 15.0

    def read_data(self):
        self.internal_temp += 0.2
        self.external_temp += 0.1
        return {'internal_temp': self.internal_temp, 'external_temp': self.external_temp}

class HumiditySensor(WirelessSensor):
    def __init__(self, sensor_id: int, hw_revision: str, loss_probability: float):
        super().__init__(sensor_id, hw_revision, loss_probability)
        self.voltage = 3.0
        n_intervals = 10
        min_v, max_v = 0.0, 5.0
        step = (max_v - min_v) / (n_intervals - 1)
        self.v_table = [min_v + i * step for i in range(n_intervals)]

        def voltage_to_percent(v: float) -> float:
            idx = min(range(len(self.v_table)), key=lambda i: abs(self.v_table[i] - v))
            return (idx + 1) * 100.0 / len(self.v_table)

        self.v_to_percent = voltage_to_percent
        self.humidity = self.v_to_percent(self.voltage)
        self.humidity = 30.0

    def read_data(self):
        self.voltage += 0.05
        self.humidity += 1.0
        return {'voltage': self.voltage, 'humidity': self.humidity}

class BatterySensor(WirelessSensor):
    def __init__(self, sensor_id: int, hw_revision: str, loss_probability: float, voltage: float = 4.2, capacity: float = 100.0, drain: float = 0.01):
        super().__init__(sensor_id, hw_revision, loss_probability)
        self.voltage = voltage
        self.capacity = capacity
        self.drain = drain

    def read_data(self):
        if super().read_data() is None:
            return None

        self.voltage = max(0.0, self.voltage - self.drain)
        self.capacity = max(0.0, self.capacity - (self.drain * 10.0))
        return {'voltage': round(self.voltage, 3), 'capacity': round(self.capacity, 2)}
    
class TelemetryPacket:
    def __init__(self, packet_id: int, timestamp: int, data: dict):
        self.packet_id = packet_id
        self.timestamp = timestamp
        self.data = data

class TelemetryLog:
    def __init__(self):
        self.packets = []

    def add_packet(self, packet: TelemetryPacket):
        self.packets.append(packet)

    def get_packets_in_interval(self, start_ts: int, end_ts: int):
        return [p for p in self.packets if start_ts <= p.timestamp <= end_ts]

    def get_error_rate(self, hw_revision: str):
        total_packets = 0
        error_packets = 0
        for packet in self.packets:
            for sensor_data in packet.data.values():
                if sensor_data['hw_revision'] == hw_revision:
                    total_packets += 1
                    if sensor_data.get('checksum') == 'corrupted':
                        error_packets += 1
        return (error_packets / total_packets) * 100.0 if total_packets > 0 else 0.0

    def is_inside_gps_polygon(self, x: float, y: float):
        gps_points = []
        for p in self.packets:
            for sensor_obj, data in p.data.items():
                if isinstance(sensor_obj, GPSSensor) and 'x' in data and 'y' in data:
                    gps_points.append((data['x'], data['y']))
        if not gps_points:
            return False
        xs = [pt[0] for pt in gps_points]
        ys = [pt[1] for pt in gps_points]

        return min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys)

def main():
    if len(argv) != 2:
        print("Usage: sensors_sim.py <number_of_steps>")
        exit(1)

    num_steps = int(argv[1])
    sensors = [
        GPSSensor(0x10, "HW_1"),
        SteeringSensor(0x11, "HW_1"),
        TemperatureSensor(0x12, "HW_2", 0.1),
        HumiditySensor(0x13, "HW_2", 0.1),
        GPSSensor(0x14, "HW_3", 5.0, 5.0),
        GPSSensor(0x15, "HW_3", 10.0, 0.0),
        BatterySensor(0x16, "HW_4", 0.05)
    ]

    telemetry_log = TelemetryLog()

    for step in range(num_steps):
        packet_data = {}
        for sensor in sensors:
            data = sensor.read_data()
            if data is not None:
                data['hw_revision'] = sensor.hw_revision
                if 'checksum' not in data:
                    if isinstance(sensor, WiredSensor):
                        data['checksum'] = sensor.calculate_checksum(data)
                packet_data[sensor] = data
        packet = TelemetryPacket(step, step, packet_data)
        telemetry_log.add_packet(packet)

    # Interactive loop
    def format_sensor_entry(sensor_obj, data):
        class_name = sensor_obj.__class__.__name__
        sensor_id = hex(sensor_obj.sensor_id)
        hw = data.get('hw_revision', "?")
        data_values = {k: v for k, v in data.items() if k not in ('hw_revision', 'checksum')}
        return f"{class_name}<{sensor_id}, \"{hw}\">: {data_values}"

    def print_packet(packet: TelemetryPacket):
        print("{")
        print(f"  Packet id: {packet.packet_id}, timestamp: {packet.timestamp}")
        print("  data: {")
        for sensor_obj, data in packet.data.items():
            print("    " + format_sensor_entry(sensor_obj, data))
        print("  }")
        print("}")

    def interactive_loop(log: TelemetryLog):
        print("Entering interactive mode. Commands:")
        print("  I <start_ts> <end_ts>   -> show packets in interval")
        print("  H <hw_rev>              -> show % of corrupted packets for hw_rev")
        print("  P <x> <y>               -> True if point inside GPS polygon")
        print("  Q                       -> quit")
        try:
            while True:
                line = input("> ").strip()
                if not line:
                    continue
                parts = line.split()
                cmd = parts[0].upper()
                if cmd == "Q":
                    break
                if cmd == "I":
                    if len(parts) != 3:
                        print("Usage: I <start_ts> <end_ts>")
                        continue
                    try:
                        start_ts = int(parts[1])
                        end_ts = int(parts[2])
                    except ValueError:
                        print("start_ts and end_ts must be integers")
                        continue
                    packets = log.get_packets_in_interval(start_ts, end_ts)
                    if not packets:
                        print("No packets in interval")
                    else:
                        for p in packets:
                            print_packet(p)
                    continue
                if cmd == "H":
                    if len(parts) != 2:
                        print("Usage: H <hw_rev>")
                        continue
                    hw = parts[1]
                    pct = log.get_error_rate(hw)
                    print(f"Error rate for {hw}: {pct:.2f}%")
                    continue
                if cmd == "P":
                    if len(parts) != 3:
                        print("Usage: P <x> <y>")
                        continue
                    try:
                        x = float(parts[1]); y = float(parts[2])
                    except ValueError:
                        print("x and y must be numbers")
                        continue
                    result = log.is_inside_gps_polygon(x, y)
                    print(str(result))
                    continue
                print("Unknown command")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting interactive mode.")

    interactive_loop(telemetry_log)

if __name__ == "__main__":
    main()