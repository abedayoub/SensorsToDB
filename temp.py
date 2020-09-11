import serial 
import time
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
import shlex

dbConn = MySQLdb.connect("localhost","root","","tempdb")
#open a cursor to the database
cursor = dbConn.cursor()

#fig = plt.figure()
#rect = plt.patch()
#ax1 = plt.axes()
flag = 0
device = 'COM3' #this will have to be changed to the serial port you are using
try:
  print("Trying...",device) 
  arduino = serial.Serial(device, 9600) 
except:
  print("Failed to connect on",device)

while True:
    try:
      time.sleep(2)
      data = arduino.readline()#read the data from the arduino
      str(data)
      print(data)
#      temps = data.split();

#      Decimal(temps[0])
#      Decimal(temps[1])
#      temps = shlex.split(data)
      temps = data.split()
      x=0
#      Decimal(temps)
      
      #Here we are going to insert the data into the Database
      #for x in range (len(temps)):
      print(temps)
      try:
          cursor.execute("INSERT INTO tempData (Temperature,Temperature2) VALUES (%s,%s)", (temps[0],temps[1]))
          dbConn.commit() #commit the insert
          
              
        
#          cursor.execute("SELECT Date from tempData")
#          path_exec = cursor.fetchall()
#          i=0
#          path_list = path_exec[i][0]
#          while(i<len(path_exec)):
#          path_list = path_exec[i][0]
#          i = i + 1
        

#        for x in range(len(path_list)):
#            print(path_list[x])
        
     
#        cursor.execute("SELECT Temperature from tempData")
#        path_exec1 = cursor.fetchall()
#        i=0
#        path_list1 = path_exec1[i][0]
#        while(i<len(path_exec1)):
#          path_list1 = path_exec1[i][0]
#          i = i + 1
          

      #  cursor.close()  #close the cursor
      except MySQLdb.IntegrityError:
        print("failed to insert data")  
          
#      finally:
#        cursor.close()  #close just incase it failed
    except:
      print("Failed to get data from Arduino!")