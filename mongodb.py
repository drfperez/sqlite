import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

# Connecta a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["exemple_db"]
col = db["empleats"]

# Defineix les funcions CRUD
def afegir_fila():
    # Obtenir les dades dels textbox
    id = id_entry.get()
    nom = nom_entry.get()
    edat = edat_entry.get()
    sou = sou_entry.get()
    
    # Inserir les dades a MongoDB
    nou_empleat = {"_id": id, "nom": nom, "edat": edat, "sou": sou}
    col.insert_one(nou_empleat)
    
    # Actualitzar la taula
    mostrar_taula()

def actualitzar_fila():
    # Obtenir les dades dels textbox
    id = id_entry.get()
    nom = nom_entry.get()
    edat = edat_entry.get()
    sou = sou_entry.get()
    
    # Actualitzar les dades a MongoDB
    col.update_one({"_id": id}, {"$set": {"nom": nom, "edat": edat, "sou": sou}})
    
    # Actualitzar la taula
    mostrar_taula()

def esborrar_fila():
    # Obtenir l'ID de la fila seleccionada
    fila_sel = taula.focus()
    id_sel = taula.item(fila_sel)['values'][0]
    
    # Esborrar la fila seleccionada de MongoDB
    col.delete_one({"_id": id_sel})
    
    # Actualitzar la taula
    mostrar_taula()

def mostrar_taula():
    # Esborrar les dades actuals de la taula
    taula.delete(*taula.get_children())
    
    # Obté les dades de la base de dades
    dades = col.find()
    
    # Mostra les dades a la taula
    for dada in dades:
        taula.insert("", "end", values=(dada["_id"], dada["nom"], dada["edat"], dada["sou"]))

# Crea la finestra principal
root = tk.Tk()
root.title("Gestió d'empleats")

# Crea les etiquetes i les entrades per a les dades
id_lbl = tk.Label(root, text="ID")
id_lbl.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

nom_lbl = tk.Label(root, text="Nom")
nom_lbl.grid(row=1, column=0)
nom_entry = tk.Entry(root)
nom_entry.grid(row=1, column=1)

edat_lbl = tk.Label(root, text="Edat")
edat_lbl.grid(row=2, column=0)
edat_entry = tk.Entry(root)
edat_entry.grid(row=2, column=1)

sou_lbl = tk.Label(root, text="Sou")
sou_lbl.grid(row=3, column=0)
sou_entry = tk.Entry(root)
sou_entry.grid(row=3, column=1)

# Crea els botons per a les operacions CRUD
afegir_btn = tk.Button(root, text="Afegir", command=afegir_fila)
afegir_btn.grid(row=4, column=0)

actualitzar_btn = tk.Button(root, text="Actualitzar", command=actualitzar_fila)
actualitzar_btn.grid(row=4, column=1)

esborrar_btn = tk.Button(root, text="Esborrar", command=esborrar_fila)
esborrar_btn.grid(row=4, column=2)

#Crea la taula per mostrar les dades
taula = ttk.Treeview(root, columns=("ID", "Nom", "Edat", "Sou"), show="headings")
taula.grid(row=5, columnspan=4)

taula.heading("ID", text="ID")
taula.heading("Nom", text="Nom")
taula.heading("Edat", text="Edat")
taula.heading("Sou", text="Sou")

#Mostra les dades a la taula inicialment
mostrar_taula()

#mostrar_taula()

Inicia la finestra
root.mainloop()
