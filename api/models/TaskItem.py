from ..database import DatabaseConnection


class item:
    def __init__(self, id_item, detalles, completado, id_tarea):
        self.id_item = id_item
        self.detalles = detalles
        self.completado = completado
        self.tarea = id_tarea
        

    @classmethod
    def create_item(cls, item):
        query= '''
        INSERT INTO item (detalles, completado)
        VALUES (%s, %s)
        '''
        
        values = (item.detalles, item.completado)
        
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True