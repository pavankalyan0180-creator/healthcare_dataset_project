import sqlite3
conn=sqlite3.connect("database/hospital.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE patients(
               IP_NO TEXT,
               Name TEXT,
               Age INTEGER,
               Gender TEXT,
               Mode_of_Arrival TEXT,
               Reason_for_Arrival TEXT,
               Chief_complaints TEXT,
               bp TEXT,
               pr TEXT,
               rr TEXT,
               Past_history TEXT,
               Present_history TEXT,
               Family_history TEXT,
               Diagnosis TEXT,
               Admission_date TEXT,
               Discharge_date TEXT,
               Length_of_stay INTEGER
               )
            """)
conn.commit()
conn.close()
print ("Database created Successfully")