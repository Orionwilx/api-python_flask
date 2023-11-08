import psycopg2

# Configura la conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",  # Reemplaza con el nombre de tu base de datos
    user="wilx",       # Reemplaza con el nombre de tu usuario
    password="w123456789", # Reemplaza con tu contraseña
    host="localhost",        # O la dirección del contenedor si es diferente
    port="5432"              # El puerto mapeado al contenedor
)

# Crea un cursor para ejecutar comandos SQL
cursor = conn.cursor()

#Creando  las columnas
create_table_query = """
CREATE TABLE tareas_db (
    id serial PRIMARY KEY,
    tarea VARCHAR (80),
    completada BOOLEAN


);
"""

cursor.execute(create_table_query)
conn.commit()

# Inserta datos en la tabla
insert_data_query = "INSERT INTO tareas_db (tarea, completada) VALUES (%s, %s)"
datos = [("comer", False), ("estudiar", False), ("comprar", False)]

for dato in datos:
    cursor.execute(insert_data_query, dato)
conn.commit()

# Ejecuta comandos SQL, por ejemplo:
cursor.execute("SELECT * FROM tareas_db")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cierra el cursor y la conexión
cursor.close()
conn.close()

# 
