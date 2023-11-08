from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wilx:w123456789@localhost/postgres'
db = SQLAlchemy(app)

# Definición de un modelo de datos
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    completada = db.Column(db.Boolean, default=False)

# Creación de la tabla en la base de datos
with app.app_context():
    db.create_all()

# Agregar datos a la base de datos
with app.app_context():
    tarea1 = Tarea(nombre='Comprar víveres', descripcion='Ir al supermercado', completada=False)
    tarea2 = Tarea(nombre='Lavar el auto', descripcion='En la gasolinera', completada=True)

# Agregar las tareas a la sesión y confirmar la transacción
    db.session.add(tarea1)
    db.session.add(tarea2)
    db.session.commit()

# Consultar las tareas en la base de datos
with app.app_context():
    tareas = Tarea.query.all()

# Imprimir las tareas
for tarea in tareas:
    print(f'Tarea: {tarea.nombre}, Descripción: {tarea.descripcion}, Completada: {tarea.completada}')
