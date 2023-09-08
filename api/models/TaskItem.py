from ..database import DatabaseConnection


class Item:
    def __init__(self, id_item, detalle, completado, id_tarea):
        self.id_item = id_item
        self.detalle = detalle
        self.completado = completado
        self.id_tarea = id_tarea

    @classmethod
    def create_item(cls, item):
        query= '''
        INSERT INTO item (detalle, completado ,fk_tarea)
        VALUES (%s, %s ,%s)
        '''
        
        values = (item.detalle, item.completado, item.id_tarea)
        
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True