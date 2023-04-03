#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3

conn = sqlite3.connect('d3_ti_2023')

print ("Opened database successfully")


# In[9]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

#creating table
studentRecord = """CREATE TABLE Mahasiswa (
                   NIM VARCHAR (10) NOT NULL,
                   NAMA VARCHAR (30),
                   ALAMAT VARCHAR (255),
                   MATA_KULIAH VARCHAR (10),
                   KELAS VARCHAR (10),
                   DOSEN_PEMBIMBING VARCHAR (30),
                   TAHUN_MASUK INT
                   )"""

#table created
cursorObject.execute(studentRecord)

#Disconnect
dataBase.close()


# In[10]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

#creating table
studentRecord = """CREATE TABLE Dosen (
                   NIP VARCHAR (20) NOT NULL,
                   NAMA_DOSEN VARCHAR (50),
                   MATA_KULIAH_YANG_DIAJAR VARCHAR (50),
                   TAHUN_MENGAJAR INT,
                   BANYAK_KELAS_YANG_DIAJAR INT,
                   TAHUN_PENSIUN INT,
                   ALAMAT VARCHAR (50)
                   )"""

#table created
cursorObject.execute(studentRecord)

#Disconnect
dataBase.close()


# In[11]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

#creating table
studentRecord = """CREATE TABLE Mata_Kuliah (
                   KODE_MATKUL VARCHAR (10),
                   NAMA_MATKUL VARCHAR (50),
                   WAKTU DATE,
                   RUANGAN VARCHAR (10),
                   DOSEN_PENGAMPU VARCHAR (50),
                   SKS INT
                   )"""

#table created
cursorObject.execute(studentRecord)

#Disconnect
dataBase.close()


# In[12]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, NAMA_DOSEN, MATA_KULIAH_YANG_DIAJAR, TAHUN_MENGAJAR, BANYAK_KELAS_YANG_DIAJAR, TAHUN_PENSIUN, ALAMAT) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("673262787", "Pak Yusuf", "wireless", "2012", "4", "-", "-"),
       ("112489382", "Bu Nur", "sistem operasi", "2014", "2", "-", "-"),
       ("339922811", "Bu Masbahah", "praktik web", "2015", "5", "-", "-"),
       ("893282918", "Bu Trisna", "statistika", "2012", "1", "-", "-")
       
      ]

cursorObject.executemany (sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[13]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_Kuliah (KODE_MATKUL, NAMA_MATKUL, WAKTU, RUANGAN, DOSEN_PENGAMPU, SKS) VALUES (%s, %s, %s, %s, %s, %s)"
val = [("23678889",  "Wireless", "2023-1-1", "Lab 3", "Pak Yusuf", 2),
       ("45332234",  "sitem operasi", "2023-1-1", "Daring", "Bu Nur", 2),
       ("65545556",  "praktik web", "2023-1-1", "Lab 2", "Bu Masbahah", 2),
       ("66755531",  "statistika", "13", "Daring", "Bu Trisna", 2)
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[16]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAMA, ALAMAT, MATA_KULIAH, KELAS, DOSEN_PEMBIMBING, TAHUN_MASUK) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ("V3922041", "Subekti Bimo Wicaksono", "Magetan", "praktik web", "TI-E", "Bu Masbahah", "2022"),
       
        
cursorObject.executemany (sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[17]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

query = "SELECT NAMA_MATKUL, DOSEN_PENGAMPU FROM Mata_Kuliah"
cursorObject.execute (query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[18]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAMA, ALAMAT, MATA_KULIAH, KELAS, DOSEN_PEMBIMBING, TAHUN_MASUK) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("V3922034", "Muhammad Rafi Naufal P", "solo", "Statistika", "TI-E", "Bu Trisna", "2022"),
       ("V3922045", "Wahyu Bagas Dwi P", "sidoarjo", "wireless", "TI-E", "pak yusuf", "2022"),
       ("V3922046", "Wahyu Ramadhan", "sidoarjo", "sistem operasi", "TI-E", "Bu Nur", "2022")
      ]
       
        
cursorObject.executemany (sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[ ]:




