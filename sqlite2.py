import tkinter as tk
import sqlite3

# Funció per a afegir una fila a la taula
def afegir_fila():
    id = int(id_entry.get())
    nom = nom_entry.get()
    edat = int(edat_entry.get())
    sou = float(sou_entry.get())
    conn.execute(f"INSERT INTO empleats (id, nom, edat, sou) VALUES ({id}, '{nom}', {edat}, {sou})")
    conn.commit()
    mostrar_taula()

# Funció per a actualitzar una fila de la taula
def actualitzar_fila():
    id = int(id_entry.get())
    nom = nom_entry.get()
    edat = int(edat_entry.get())
    sou = float(sou_entry.get())
    conn.execute(f"UPDATE empleats SET nom = '{nom}', edat = {edat}, sou = {sou} WHERE id = {id}")
    conn.commit()
    mostrar_taula()

# Funció per a esborrar una fila de la taula
def esborrar_fila():
    id = int(id_entry.get())
    conn.execute(f"DELETE FROM empleats WHERE id = {id}")
    conn.commit()
    mostrar_taula()

# Funció per a mostrar la taula
def mostrar_taula():
    taula.delete(*taula.get_children())
    cursor = conn.execute("SELECT * FROM empleats")
    for fila in cursor:
        taula.insert("", "end", values=fila)

# Connecta't a la base de dades
conn = sqlite3.connect('exemple.db')

# Crea la interfície d'usuari
root = tk.Tk()
root.title("Exemple de base de dades")

# Crea les etiquetes i les entrades per a les dades
id_label = tk.Label(root, text="ID")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

nom_label = tk.Label(root, text="Nom")
nom_label.grid(row=1, column=0)
nom_entry = tk.Entry(root)
nom_entry.grid(row=1, column=1)

edat_label = tk.Label(root, text="Edat")
edat_label.grid(row=2, column=0)
edat_entry = tk.Entry(root)
edat_entry.grid(row=2, column=1)

sou_label = tk.Label(root, text="Sou")
sou_label.grid(row=3, column=0)
sou_entry = tk.Entry(root)
sou_entry.grid(row=3, column=1)

# Crea els botons per a les operacions CRUD
afegir_btn = tk.Button(root, text="Afegir", command=afegir_fila)
afegir_btn.grid(row=4, column=0)

actualitzar_btn = tk.Button(root, text="Actualitzar", command=actualitzar_fila)
actualitzar_btn.grid(row=4, column=1)

esborrar_btn = tk.Button(root, text="Esborrar", command=esborrar_fila)
esborrar_btn.grid(row=4, column=2)

# Crea la taula per a mostrar les dades
taula = tk.ttk.Treeview(root, columns=("ID", "Nom", "Edat", "Sou"))
taula.heading("#0", text="")
taula.heading("ID", text="ID")
taula.heading("Nom", text="Nom")
taula.heading("Edat", text="Edat")
taula.heading("Sou", text="Sou")
taula.grid(row=5, column=0, columnspan=3)

# Mostra la taula inicialment
mostrar_taula()

# Inicia l'aplicació
root.mainloop()

# Tanca la connexió a la base de dades
conn.close()

