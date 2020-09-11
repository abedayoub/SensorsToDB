import serial 
import time
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
import pandas as pd
import pyodbc

dbConn = MySQLdb.connect("localhost","root","","tempdb")

cursor = dbConn.cursor()
        
Data = namedtuple('Data','ID Temp1 Temp2 DateTime')

query = "SELECT Temperature,Temperature2 ,Date from tempData"
cursor.execute("SELECT Temperature,Temperature2 ,Date from tempData")
path_exec = cursor.fetchall()
print(path_exec)
df = pd.read_sql(query, dbConn, index_col=['Date'])
fig, ax = plt.subplots()
df.plot(ax=ax)
print(df.describe())
print(df.head())
dbConn.close()


 
#data = cursor.fetchall()



# close cursor and connection
#cursor.close()
#dbConn.close()

# unpack data in TimeStamp (x axis) and Pac (y axis)
#Date, Temperature = zip(*data)

# graph code
#plt.plot(Date, Temperature, align='center')

# set title, X/Y labels
#plt.title("Plotting Test")
#plt.xlabel("Date")
#plt.ylabel("Temperature")
#fig = plt.gcf()

# plt.xticks(TimeStamp, (hour))
#fig.set_size_inches(20.5,10.5)
#plt.grid(True)
#plt.draw()
#fig.savefig('test2.png', dpi=100)

   
#for x in range(len(path_exec)):
#    string'x' = "Hello"
#    print(dataRow3)

#for x in range(len(path_exec)):
#    pieces = dataRow.split()
    


#for i in range(len(path_exec[0])):
    