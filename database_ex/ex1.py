import sqlite3

def create_database():
    con = sqlite3.connect("retn.db")
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_retention (
                   retn_code TEXT,
                   desc TEXT,
                   nutr_no TEXT,
                   nutr_desc TEXT,
                   retn_factor REAL,
                   PRIMARY KEY (retn_code, nutr_no)
                   )                   
''')
    
    con.commit()
    con.close()
    print("Created database food_retention")

def parse_and_insert_data():
    con = sqlite3.connect("retn.db")
    cursor = con.cursor()

    with open('retn5_dat.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split('^')

        if len(parts) >= 5:
            retn_code = parts[0].strip('~')
            desc = parts[1].strip('~')
            nutr_no = parts[2].strip('~')
            nutr_desc = parts[3].strip('~')

            retn_factor_str = parts[4].strip('~')
            if retn_factor_str:
                retn_factor = int(retn_factor_str)
            else:
                retn_factor = None

            cursor.execute('''INSERT OR REPLACE INTO food_retention 
                           (retn_code, desc, nutr_no, nutr_desc, retn_factor) 
                           VALUES (?, ?, ?, ?, ?)''',
                            (retn_code, desc, nutr_no, nutr_desc, retn_factor))
    con.commit()
    con.close()

def find_veal_foods():
    con = sqlite3.connect("retn.db")
    cursor = con.cursor()

    cursor.execute('''
    SELECT retn_code, desc, nutr_no, nutr_desc, retn_factor
                   FROM food_retention
                   WHERE desc LIKE '%VEAL%'                   
''')
    result = cursor.fetchall()

    for row in result:
        retn_code, desc, nutr_no, nutr_desc, retn_factor = row
        print(f"{retn_code} {desc} {nutr_no} {nutr_desc} {retn_factor}")
    print("Count:", len(result))
    con.close()

if __name__ == "__main__":
    create_database()
    parse_and_insert_data()
    find_veal_foods()