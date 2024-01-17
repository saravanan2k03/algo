import mysql.connector
import openpyxl

mydb = mysql.connector.connect(host="10.201.137.11", user="getdata", password="data@3908", database="energy_meter")
mycursor = mydb.cursor()

query = "SELECT * FROM modbusvalues1 WHERE createddt > %s"
params = ('2023-06-26',)
mycursor.execute(query, params)
myresult = mycursor.fetchall()

col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ']

bk = openpyxl.load_workbook('en.xlsx')
sh = bk['Sheet1']

cell_range = 'A2:' + col[len(myresult[0])-1] + str(len(myresult)+1)
sh.append([cell.value for row in myresult for cell in row])

bk.save(filename='en.xlsx')
print('saved')
