<<<<<<< HEAD
from ..models.TaskItem import Item
=======
from ..models.Tasks import Tarea
>>>>>>> main
from flask import request,jsonify

class ItemController():
    @classmethod
    def create_item(self):
        data = request.json
        print(data)
        item = Item(
            id_item= None,
            detalle=data['detalle'],
            completado=data['completado'],
            id_tarea=data['fk_tarea'],
        )
        item.create_item(item)
        return jsonify({}), 201
    