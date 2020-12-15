import time
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot as plt
from collections import namedtuple
import pandas as pd


dbConn = MySQLdb.connect("localhost","root","","tempdb") #or MySQLdb.die("can't")

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