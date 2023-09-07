from ..models.Tasks import tarea
from flask import request,jsonify

class TareaController:
    @classmethod
    def get_all_tasks(cls):
        tarea_lista = tarea.get_all_tasks()
        
        response = []
        
        for tarea in tarea_lista:
            categoria = tarea.get("categoria", {})
            item = tarea.get("item", {})
            tarea_data = {
                "categoria": {
                    "nombre": categoria.get("nombre", ""),
                    
                },
                "item" : {
                    "detalles" : item.get("detalles", ""),
                },
                "id_tarea" : tarea.get("id_tarea", ""),
                "nombre" : tarea.get("nombre", ""),
                "fecha_creacion" : tarea.get("fecha_creacion", ""),
                "fecha_limite" : tarea.get("fecha_limite", ""),
                "completada": tarea.get("completada", "")
            }
            response.append(tarea_data)
        return jsonify(response),200
    
    @classmethod
    def get_task_by_id(self,id_tarea):
        tarea = tarea.get_task_by_id(id_tarea)
        if tarea:
            response = {
                "id_tarea" : tarea.get("id_tarea", ""),
                "nombre" : tarea.get("nombre", ""),
                "fecha_creacion" : tarea.get("fecha_creacion", ""),
                "fecha_limite" : tarea.get("fecha_limite", ""),
                "completada": tarea.get("completada", "")
            }
            return jsonify(response),200
        else:
            return jsonify({"error": "tarea no encontrada"}),404
    
    @classmethod
    def create_task(self):
        data = request.json
        tarea = tarea(
            id_tarea = None,
            nombre = data.get('nombre'),
            fecha_creacion = data.get('fecha_creacion'),
            fecha_limite = data.get('fecha_limite'),
            completada = data.get('completada')
        )
        tarea.create_task(tarea)
        return jsonify({}), 201