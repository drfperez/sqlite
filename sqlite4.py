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
    query += " OR price < 10"
    c.execute(query)
    results = c.fetchall()
    display_results(results)

# Set up tkinter interface
root = Tk()

# Define labels and entry fields for each item
label1 = Label(root, text="ID")
label1.grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Name")
label2.grid(row=1, column=0)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

label3 = Label(root, text="Category")
label3.grid(row=2, column=0)
entry3 = Entry(root)
entry3.grid(row=2, column=1)

label4 = Label(root, text="Price")
label4.grid(row=3, column=0)
entry4 = Entry(root)
entry4.grid(row=3, column=1)

label5 = Label(root, text="In Stock")
label5.grid(row=4, column=0)
entry5 = Entry(root)
entry5.grid(row=4, column=1)

# Define buttons
button1 = Button(root, text="Create", command=create)
button1.grid(row=5, column=0)

button2 = Button(root, text="Read", command=read)
button2.grid(row=5, column=1)

button3 = Button(root, text="Update", command=update)
button3.grid(row=5, column=2)

button4 = Button(root, text="Delete", command=delete)
button4.grid(row=5, column=3)

# Define labels and entry field for select operation
select_label = Label(root, text="Select query")
select_label.grid(row=6, column=0)
select_entry = Entry(root)
select_entry.grid(row=6, column=1)
select_button = Button(root, text="Select", command=select)
select_button.grid(row=6, column=2)

# Define labels and entry field for logical operations
logical_label = Label(root, text="Logical query")
logical_label.grid(row=7, column=0)
logical_entry = Entry(root)
logical_entry.grid(row=7, column=1)
and_button = Button(root, text="AND", command=and_operation)
and_button.grid(row=7, column=2)
or_button = Button(root, text="OR", command=or_operation)
or_button.grid(row=7, column=3)

# Run tkinter interface
root.mainloop()

# Close database connection
conn.close()

