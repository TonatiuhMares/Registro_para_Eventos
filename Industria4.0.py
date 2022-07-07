import sqlite3
db = sqlite3.connect('Conferencias.db')
with db:
    cursor = db.cursor()
    sql1 = '''CREATE TABLE IF NOT EXISTS Industria4_0(ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT NOT NULL,
                Teléfono TEXT NOT NULL, Correo TEXT NOT NULL)'''
    cursor.execute(sql1)
    db.commit()
db.close()