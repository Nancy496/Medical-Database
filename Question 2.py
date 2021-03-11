#!/usr/bin/env python
# coding: utf-8

# In[12]:


import sqlite3
import csv

#Create or connect to the database
sqlite_conn = sqlite3.connect('Medical.db')

print ("Database connected")


# In[13]:


#Create a cursor object
conn = sqlite_conn.cursor()

# Print sqlite version
dbversion = conn.execute("select sqlite_version();")
print("SQLite Database Version is: ", dbversion.fetchall(), "\n")


# In[14]:


# Create hospital table
conn.execute(''' CREATE TABLE IF NOT EXISTS Hospital1
            (Hospital_id INT PRIMARY KEY NOT NULL UNIQUE,
             Hospital_Name TEXT NOT NULL,
             Bed_count INT NOT NULL);''')

# Create Doctor Table
conn.execute(''' CREATE TABLE IF NOT EXISTS Doctor1
            (  Doctor_id INT PRIMARY KEY NOT NULL,
              Doctor_Name TEXT NOT NULL,
              Hospital_id INT NOT NULL,
              Date_joined TEXT NOT NULL,
              Speciality TEXT NOT NULL,
              Salary INT NOT NULL,
              Experience TEXT NOT NULL,
              Email TEXT NOT NULL,
              UNIQUE(Doctor_id, Email)
              FOREIGN KEY (Hospital_id)
                REFERENCES Hospital1 (Hospital_id) );''')

print("Tables created")


# In[15]:


# Read from csv file
with open (r"C:\Users\User\Downloads\hospitals_Nancy.csv", 'r') as hospitalrec:
    h_reader = csv.reader(hospitalrec)
    
    next(h_reader) #Skip the first row 
    
    #insert records line by line
    for rec in h_reader:
        conn.execute("INSERT OR REPLACE INTO Hospital1 VALUES (?, ?, ?);", rec)
        sqlite_conn.commit()
print("Records added")


# In[16]:


# Read from csv file
with open(r"C:\Users\User\Downloads\doctors (2).csv", 'r') as docrec:
    d_reader = csv.reader(docrec)
    
    next(d_reader) #dkip first ecord
    for rec in d_reader:
        conn.execute(
            "INSERT OR REPLACE INTO Doctor1 VALUES (?, ?, ?, ?, ?, ?, ?, ?);", rec)
        sqlite_conn.commit()
print("Records added")


# In[19]:


def nancy_join():
    #Query to create inner join
    hos_join = conn.execute('''SELECT * FROM Doctor1 INNER JOIN Hospital1 
                        ON Hospital1.Hospital_id = Doctor1.Hospital_id;''')
    #Display records
    for j in hos_join.fetchall():
        print(j, "\n")
    
#call the function    
nancy_join()
    
#close cursor    
conn.close()


# In[ ]:




