import os
import json
import sqlite3
from datetime import datetime

folder = "Annotation_file"
conn=sqlite3.connect("database/hospital.db")
print(os.path.abspath("database/hospital.db"))
cursor= conn.cursor()
for file in os.listdir(folder):
    if file.endswith(".json"):
        with open(os.path.join(folder,file)) as f:
            data = json.load(f)

        IP_NO=data["IP_NO"]
        Name=data["Name"]
        Age=data["Age"]
        Gender=data["Gender"]
        Mode_of_Arrival=data["Mode_of_Arrival"]
        Reason_for_Arrival=data["Reason_for_Arrival"]
        Chief_complaints=",".join(data["Chief_complaints"]) if isinstance(data["Chief_complaints"], list) else data["Chief_complaints"]
        bp=data["Vital"]["bp"]
        pr=data["Vital"]["pr"]
        rr=data["Vital"]["rr"]
        Past_history=data["Past_history"]
        Present_history=data["Present_history"]
        Family_history=data["Family_history"] if data["Family_history"] is not None else " given"
        Daignosis=data["Daignosis"]
        Admission = datetime.strptime(data["Admission_date"], "%Y-%m-%d")
        Discharge = datetime.strptime(data["Discharge_date"], "%Y-%m-%d")
        LOS=(Discharge-Admission).days
        cursor.execute("""
INSERT INTO patients VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(IP_NO,Name,Age,Gender,Mode_of_Arrival,Reason_for_Arrival,Chief_complaints,bp,pr,rr,Past_history,Present_history,Family_history,Daignosis,data["Admission_date"],data["Discharge_date"],LOS))
conn.commit()
conn.close()
print("Data extracted Successfully")
