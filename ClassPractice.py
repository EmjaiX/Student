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

def insertRow(data):
    
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[1])


    sql = "INSERT INTO automobiles (MobileName, MobileMake,Transmission) VALUES (%s, %s, %s)"
    val = (data[0], data[1],data[2])

    mycursor.execute(sql, val)

    mydb.commit()


mydb = ql.connect(
  host="127.0.0.1",
  user="root",
  password="usbw",
  database="python"
)

mycursor = mydb.cursor()


readTable("automobiles")

# mycursor.execute("Select * from automobiles")



# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x[1])


# sql = "INSERT INTO automobiles (MobileName, MobileMake,Transmission) VALUES (%s, %s, %s)"
# val = ("Teresita", "Mercialargo:Lamberghini:2018","Automatic")

# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)