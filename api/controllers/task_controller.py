from ..models.Tasks import Tarea
from flask import request,jsonify
from datetime import datetime
class TareaController:
    @classmethod
    def get_all_tasks(cls):
        tarea_lista = Tarea.get_all_tareas()
        
        response = []
        
        for tarea in tarea_lista:
            tarea_data = {
                "id_tarea" : tarea["id_tarea"],
                "nombre" : tarea["nombre"],
                "fecha_creacion" : tarea["fecha_creacion"].strftime("%Y-%m-%d"),
                "fecha_limite" : tarea["fecha_limite"].strftime("%Y-%m-%d"),
                "completada": tarea["completada"]
            }
            response.append(tarea_data)
        return jsonify(response),200
    
    @classmethod
    def get_task_by_id(self,id_tarea):
        tarea = tarea.get_task_by_id(id_tarea)
        if tarea:
            response = {
            "id_tarea": tarea.id_tarea,
            "nombre": tarea.nombre,
            "fecha_creacion": tarea.fecha_creacion,
            "fecha_limite": tarea.fecha_limite,
            "completada": tarea.completada,
            "id_categoria": tarea.id_categoria
            }
            return jsonify(response),200
        else:
            return jsonify({"error": "tarea no encontrada"}),404
    
    @classmethod
    def create_task(self):
        data = request.json
        tarea = Tarea(
            id_tarea = None,
            nombre = data.get('nombre'),
            fecha_creacion = data.get('fecha_creacion'),
            fecha_limite = data.get('fecha_limite'),
            completada = data.get('completada'),
            id_categoria=data.get('id_categoria')
        )
        Tarea.create_tarea(tarea)
        return jsonify({}), 201