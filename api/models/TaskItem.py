from ..database import DatabaseConnection


class item:
    def __init__(self, id_item, detalles, completado, id_tarea):
        self.id_item = id_item
        self.detalles = detalles
        self.completado = completado
        self.tarea = id_tarea
        

    