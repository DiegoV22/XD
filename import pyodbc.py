import pyodbc

# Configuración de la conexión a SQL Server
name_server = 'DESKTOP-DFK7EV6\\SQLEXPRESS'
database = 'MundoPeluche'
username = 'GerenteGeneral'
password = 'Peluche22'
controlador_odbc = 'SQL Server'

connection_string = f'DRIVER={{SQL Server}};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

# Función para insertar un cliente
def insertar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        print("\nINSERTAR NUEVO CLIENTE")
        nombre = input("Nombre: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        tipo_cliente = input("Tipo de cliente (Empresa o Particular): ")
        
        query = """
        INSERT INTO Clientes.Cliente (nombre, email, teléfono, dirección, tipo_cliente)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (nombre, email, telefono, direccion, tipo_cliente))
        conexion.commit()
        print("Cliente agregado con éxito.")
    except Exception as e:
        print("Error al insertar cliente:", e)

# Función para consultar todos los clientes
def consultar_clientes(conexion):
    try:
        cursor = conexion.cursor()
        print("\nLISTADO DE CLIENTES")
        query = "SELECT * FROM Clientes.Cliente"  # Esquema explícito
        cursor.execute(query)
        registros = cursor.fetchall()
        for r in registros:
            print(f"ID: {r[0]}, Nombre: {r[1]}, Email: {r[2]}, Teléfono: {r[3]}, Dirección: {r[4]}, Tipo: {r[5]}")
    except Exception as e:
        print("Error al consultar clientes:", e)

# Función para actualizar un cliente
def actualizar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        print("\nACTUALIZAR CLIENTE")
        id_cliente = int(input("ID del cliente a actualizar: "))
        nuevo_telefono = input("Nuevo teléfono: ")
        nueva_direccion = input("Nueva dirección: ")
        
        query = """
        UPDATE Clientes.Cliente
        SET teléfono = ?, dirección = ?
        WHERE id_cliente = ?
        """
        cursor.execute(query, (nuevo_telefono, nueva_direccion, id_cliente))
        conexion.commit()
        print("Cliente actualizado con éxito.")
    except Exception as e:
        print("Error al actualizar cliente:", e)

# Función para eliminar un cliente
def eliminar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        print("\nELIMINAR CLIENTE")
        id_cliente = int(input("ID del cliente a eliminar: "))
        
        query = "DELETE FROM Clientes.Cliente WHERE id_cliente = ?"
        cursor.execute(query, (id_cliente,))
        conexion.commit()
        print("Cliente eliminado con éxito.")
    except Exception as e:
        print("Error al eliminar cliente:", e)

# Función para mostrar opciones CRUD
def mostrar_opciones_crud():
    print("\nSISTEMA CRUD - Clientes")
    print("1. Crear cliente")
    print("2. Consultar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")

# Función principal
def main():
    try:
        conexion = pyodbc.connect(connection_string)
        while True:
            mostrar_opciones_crud()
            opcion = input("Seleccione una opción (1-5): ")
            if opcion == '1':
                insertar_cliente(conexion)
            elif opcion == '2':
                consultar_clientes(conexion)
            elif opcion == '3':
                actualizar_cliente(conexion)
            elif opcion == '4':
                eliminar_cliente(conexion)
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
    finally:
        if 'conexion' in locals():
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    main()
