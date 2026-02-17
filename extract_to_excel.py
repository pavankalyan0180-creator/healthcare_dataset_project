import sqlite3

import pandas as pd

conn=sqlite3.connect("database/hospital.db")

df=pd.read_sql_query("SELECT * FROM patients",conn)

df.to_excel("output/patient-dataset.xlsx",index=False)

conn.close()
print("Excel file created")