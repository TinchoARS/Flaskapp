from ..database import DatabaseConnection

class categoria:
    def __init__(self, id_categoria, nombre, descripcion,):
        self.id_categoria = id_categoria
        self.nombre = nombre 
        self.descripcion = descripcion
        
    @classmethod
    def create_categoria(cls, categoria):
        query = '''
        INSERT INTO categoria (nombre, descripcion)
        VALUES (%s, %s)
        '''
        values = (categoria.nombre, categoria.descripcion)
        
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, categoria)
        connection.commit()
        cursor.close()
        return True