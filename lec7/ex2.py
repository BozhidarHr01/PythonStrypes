import math

class Projectile:
    def __init__(self, mass, x, y=0):
        self.mass = mass
        self.x0 = x
        self.y0 = y

    def shoot(self, angle, speed):
        angle_rad = math.radians(angle)
        vx = speed * math.cos(angle_rad)
        vy = speed * math.sin(angle_rad)
        g = 9.81
        t = 0
        dt = 0.1
        print("t,x,y")
        while True:
            x = self.x0 + vx * t
            y = self.y0 + vy * t - 0.5 * g * t**2
            if y < 0:
                break
            print(f"{t:.2f},{x:.2f},{y:.2f}")
            t += dt

if __name__ == "__main__":
    mass = float(input("Enter mass: "))
    x = float(input("Enter initial x: "))
    angle = float(input("Enter angle (degrees): "))
    speed = float(input("Enter initial speed: "))
    p = Projectile(mass, x)
    p.shoot(angle, speed)
