import tkinter
import pyodbc

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost;"
            "Database=El_Time_Facebook;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()
cursor.execute("SELECT * from FaceBookGroupsTest")
cnxn.commit()