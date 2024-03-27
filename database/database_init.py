import sqlite3
import datetime

conn = sqlite3.connect('patients.db')

c = conn.cursor()  
c.execute("""CREATE TABLE patients (
            idx text,
            f_name text,
            l_name text,
            age text,
            timestamp text,
            previous_hash text,
            proof text
            )""")
conn.commit()
conn.close()
