from ..models.Tasks import Tarea
from flask import request,jsonify

class CategoryController():
    @classmethod
    def create_category(self):
        data = request.json
        categoria = categoria(
            id_categoria= None,
            nombre=data('nombre'),
            descripcion=data('descripcion')  
        )
        categoria.create_category(categoria)
        return jsonify({}), 201
    