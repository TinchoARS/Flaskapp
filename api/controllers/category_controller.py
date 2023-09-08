<<<<<<< HEAD
from ..models.Tasks import tarea
from flask import request,jsonify
=======
>>>>>>> dcbc635573a6fc4a5bfe3dd31b2bc09c8b3f46ea
from ..models.Category import Categoria
from flask import request,jsonify


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
    
