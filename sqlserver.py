import pyodbc


connstring_users='DRIVER={SQL Server};SERVER=103.207.1.94;DATABASE=attendance;PORT=1433;UID=ReadOnly1;PWD=ReadOnly@123;ENCRYPT=no;Trusted_Connection=yes;'

server = '103.207.1.94'
db1='attendance'
tcon='yes'
uname='ReadOnly1'
pword='ReadOnly@123'
# Establish a connection
conn =  pyodbc.connect(connstring_users)
print('Connecting to')
# Create a cursor
cursor = conn.cursor()

# Execute the query
cursor.execute("SELECT * FROM appLoginData")

# Fetch and print the data
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
