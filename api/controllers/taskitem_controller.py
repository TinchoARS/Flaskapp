from ..models.Tasks import tarea
from flask import request,jsonify

class ItemController():
    @classmethod
    def create_item(self):
        data = request.json
        item = item(
            id_item= None,
            detalles=data('detalles'),
            completado=data('completado')  
        )
        item.create_item(item)
        return jsonify({}), 201
    