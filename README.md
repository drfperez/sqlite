# sqlite
Sqlite CRUD in python

Sqlite4.py
This code defines four buttons for the CRUD operations (create, read, update, and delete), as well as buttons and entry fields for select and logical operations. The tkinter interface is then set up with labels and entry fields for each item, and the buttons and entry fields for select and logical operations are placed on the interface as well. Finally, the interface is run and the database connection is closed when the interface is closed.
The select, and_operation, and or_operation functions allow the user to perform more complex queries on the database by combining selection criteria with logical operators.

For example, if the user enters "SELECT * FROM items WHERE category='Category A' AND in_stock > 0" in the select_entry field and clicks the "Select" button, the select function will execute the query and retrieve all items that belong to Category A and have more than 0 items in stock.
Similarly, if the user enters "SELECT * FROM items WHERE price < 10 OR in_stock = 0" in the logical_entry field and clicks the "OR" button, the or_operation function will execute the query and retrieve all items that have a price less than 10 or are out of stock.

sqlite5.py add two more logical operations. The or_operation function now adds the OR operator to the query and retrieves all items that have a stock greater than 0. The between_operation function adds the BETWEEN operator to the query and retrieves all items that have a price between 5 and 15.

The exists_operation function adds the EXISTS operator to the query and retrieves all items that have a category of 'Category A'.
Note that if you want to run this code, you will need to have a database file called "items.db" in the same directory as the Python script. You can create this file using the code at the beginning of the script, which creates a table called "items" and inserts some sample data.
