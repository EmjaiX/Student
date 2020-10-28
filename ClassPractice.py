import mysql.connector as ql

def readTable(TableName):
    query = "Select * from " + TableName
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def readCell(TableName,cell):
    query = "Select * from " + TableName
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[cell])

def insertRow(command,value):

    mycursor.execute(command, value)

    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

def runQuery(query):
    mycursor.execute(query)



mydb = ql.connect(
  host="127.0.0.1",
  port="3306",
  user="root",
  password="usbw",
  database="python"
)

mycursor = mydb.cursor()


readCell("automobiles",1)

# mycursor.execute("Select * from automobiles")



# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x[1])


# sql = "INSERT INTO automobiles (MobileMake,MobileName,Transmission) VALUES (%s, %s, %s)"
# val = ("Cayeman:Porche:2000", "Fort","Standard")

# insertRow(sql, val)

