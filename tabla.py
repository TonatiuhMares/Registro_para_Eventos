import sqlite3
db = sqlite3.connect('Conferencias.db')
with db:
    cursor = db.cursor()
    sql1 = '''CREATE TABLE IF NOT EXISTS Eventos(Asistentes INTEGER NOT NULL, Evento TEXT NOT NULL,
                FECHA TEXT NOT NULL, HORARIO TEXT NOT NULL)'''
    cursor.execute(sql1)
    db.commit()
db.close()
