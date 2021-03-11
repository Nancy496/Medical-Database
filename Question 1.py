#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sqlite3
conn = sqlite3.connect(':memory:')
mycursor = conn.cursor()
print("connected to memory")


# In[9]:


mycursor.execute(''' CREATE TABLE IF NOT EXISTS Hospital1
            (Hospital_id INT PRIMARY KEY NOT NULL UNIQUE,
             Hospital_Name TEXT NOT NULL,
             Bed_count INT NOT NULL);''')

print("Table created")


# In[10]:


# Display the structure of the table
ht_info = conn.execute("PRAGMA table_info('Hospital1');")
print(" \t Hospital Table Structure ")
print("__________________________________________\n")
for x in ht_info.fetchall():
    print(x)


# In[ ]:




