import sqlite3

# Connecta't a la base de dades
conn = sqlite3.connect('exemple.db')
print("Connexió establerta amb èxit a exemple.db")

# Crea una taula
conn.execute('''CREATE TABLE empleats
             (id INT PRIMARY KEY NOT NULL,
             nom TEXT NOT NULL,
             edat INT NOT NULL,
             sou REAL NOT NULL);''')
print("Taula empleats creada amb èxit")

# Inserta dades
conn.execute("INSERT INTO empleats (id, nom, edat, sou) \
              VALUES (1, 'Anna', 28, 3500.00)")
print("Dades inserides a la taula empleats")

# Edita dades
conn.execute("UPDATE empleats SET sou = 4000.00 WHERE id = 1")
print("Dades de la taula empleats actualitzades amb èxit")

# Esborra dades
conn.execute("DELETE FROM empleats WHERE id = 1")
print("Dades de la taula empleats esborrades amb èxit")

# Elimina la taula
conn.execute("DROP TABLE empleats")
print("Taula empleats eliminada amb èxit")

# Confirma els canvis i tanca la connexió
conn.commit()
conn.close()
print("Connexió tancada amb èxit")
