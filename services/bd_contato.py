from matplotlib.pyplot import text
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ta.dacio\Documents\SENDMSG_GU\db_msg.accdb;')
cursor = conn.cursor()
# cursor.execute('select * from contato_msg')
   
# for row in cursor.fetchall():
#     print (row)

# Cpff = "37890312830"

# cursor.execute(f"SELECT * from contato_msg WHERE cpf_motorista = {Cpff}") 
# row = cursor.fetchone() 

# print(row)
    