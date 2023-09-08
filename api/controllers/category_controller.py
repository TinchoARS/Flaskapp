from flask import request,jsonify
from ..models.Category import Categoria

class CategoryController():
    @classmethod
    def create_category(self ):
        data = request.json
        categoria = Categoria(
            id_categoria= None,
            nombre=data['nombre'],
            descripcion=data['descripcion']  
        )
        Categoria.crear_categoria(categoria)
        return jsonify({}), 201
    