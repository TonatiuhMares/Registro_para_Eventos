import sqlite3

class SqliteHelper:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)
            
    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def crearTabla(self):
        c = self.cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios(ID INTEGER
        PRIMARY KEY AUTOINCREMENT, Usuario TEXT NOT NULL, Contraseña INTEGER)''')
        
    def Editar(self,query,updates):
        c = self.cursor.execute(query, updates)
        self.conn.commit()

    def Borrar(self, query):
        c = self.cursor.execute(query)
        self.conn.commit()

    def Insertar(self,query,updates):
        c = self.cursor.execute(query,updates)
        self.conn.commit()

    def Seleccionar(self,query):
        c = self.cursor.execute(query)
        return self.cursor.fetchall()

