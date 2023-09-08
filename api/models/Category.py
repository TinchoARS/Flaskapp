from ..database import DatabaseConnection

class Categoria:
    def __init__(self, id_categoria, nombre, descripcion,):
        self.id_categoria = id_categoria
        self.nombre = nombre 
        self.descripcion = descripcion
        
    @classmethod
    def crear_categoria(cls, categoria):
        query = '''
        INSERT INTO categoria (nombre, descripcion)
        VALUES (%s, %s)
        '''
        values = (categoria.nombre, categoria.descripcion)

        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True