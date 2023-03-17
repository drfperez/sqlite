import sqlite3
from tkinter import *

# Connect to database
conn = sqlite3.connect('items.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS items
             (id INTEGER PRIMARY KEY,
             name TEXT,
             category TEXT,
             price REAL,
             in_stock INTEGER)''')

# Insert sample data
c.execute("INSERT INTO items (name, category, price, in_stock) VALUES (?, ?, ?, ?)", ('Item 1', 'Category A', 10.50, 5))
c.execute("INSERT INTO items (name, category, price, in_stock) VALUES (?, ?, ?, ?)", ('Item 2', 'Category B', 20.00, 2))
c.execute("INSERT INTO items (name, category, price, in_stock) VALUES (?, ?, ?, ?)", ('Item 3', 'Category A', 5.00, 10))
c.execute("INSERT INTO items (name, category, price, in_stock) VALUES (?, ?, ?, ?)", ('Item 4', 'Category B', 15.00, 0))

# Define functions for CRUD operations
def create():
    name = entry1.get()
    category = entry2.get()
    price = entry3.get()
    in_stock = entry4.get()
    c.execute("INSERT INTO items (name, category, price, in_stock) VALUES (?, ?, ?, ?)", (name, category, price, in_stock))
    conn.commit()

def read():
    id = entry1.get()
    c.execute("SELECT * FROM items WHERE id=?", (id,))
    results = c.fetchall()
    display_results(results)

def update():
    id = entry1.get()
    name = entry2.get()
    category = entry3.get()
    price = entry4.get()
    in_stock = entry5.get()
    c.execute("UPDATE items SET name=?, category=?, price=?, in_stock=? WHERE id=?", (name, category, price, in_stock, id))
    conn.commit()

def delete():
    id = entry1.get()
    c.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()

# Define function for displaying results
def display_results(results):
    for result in results:
        print(result)

# Define functions for select and logical operations
def select():
    query = select_entry.get()
    c.execute(query)
    results = c.fetchall()
    display_results(results)

def and_operation():
    query = logical_entry.get()
    query += " AND in_stock > 0"
    c.execute(query)
    results = c.fetchall()
    display_results(results)

def or_operation():
    query = logical_entry.get()
    query += " OR in_stock > 0"
    c.execute(query)
    results = c.fetchall()
    display_results(results)

def between_operation():
    query = logical_entry.get()
    query += " AND price BETWEEN 5 AND 15"
    c.execute(query)
    results = c.fetchall()
    display_results(results)

def exists_operation():
    query = logical_entry.get()
    query += " AND EXISTS (SELECT 1 FROM items WHERE category = 'Category A')"
    c.execute(query)
    results = c.fetchall()
    display_results(results)

# Create GUI
root = Tk()

# Create labels and entries for CRUD operations
Label(root, text="ID").grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)

Label(root, text="Name").grid(row=1, column=0)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

Label(root, text="Category").grid(row=2, column=0)
entry3 = Entry(root)
entry3.grid(row=2, column=1)

Label(root, text="Price").grid(row=3, column=0)
entry4 = Entry(root)
entry4.grid(row=3, column=1)

Label(root, text="In Stock").grid(row=4, column=0)
entry5 = Entry(root)
entry5.grid(row=4, column=1)

Button(root, text="Create", command=create).grid(row=5, column=0)
Button(root, text="Read", command=read).grid(row=5, column=1)
Button(root, text="Update", command=update).grid(row=5, column=2)
Button(root, text="Delete", command=delete).grid(row=5, column=3)

# Create labels and entries for select and logical operations
Label(root, text="Query").grid(row=6, column=0)
select_entry = Entry(root)
select_entry.grid(row=6, column=1)

Button(root, text="Select", command=select).grid(row=7, column=0)
Button(root, text="AND Operation", command=and_operation).grid(row=7, column=1)
Button(root, text="OR Operation", command=or_operation).grid(row=7, column=2)
Button(root, text="BETWEEN Operation", command=between_operation).grid(row=7, column=3)
Button(root, text="EXISTS Operation", command=exists_operation).grid(row=8, column=3)

# Start GUI
root.mainloop()

   
