from ..database import DatabaseConnection
from flask import Flask, request, jsonify
from datetime import datetime

class Tarea:
    def __init__(self, id_tarea, nombre, fecha_creacion, fecha_limite, completada, id_categoria):
       self.id_tarea = id_tarea
       self.nombre = nombre
       self.fecha_creacion = fecha_creacion
       self.fecha_limite = fecha_limite
       self.completada = completada
       self.id_categoria = id_categoria
              
    @classmethod
    def get_all_tareas(cls):
        query = '''
        SELECT
            tarea.id_tarea,
            tarea.nombre,
            tarea.fecha_creacion,
            tarea.fecha_limite,
            tarea.completada
        FROM
        tarea
        '''
        
        results = DatabaseConnection.fetch_all(query)
       
        tarea_list = []
        
        for result in results:
            tarea_list.append({
                "id_tarea": result[0],
                "nombre": result[1],
                "fecha_creacion": result[2],
                "fecha_limite": result[3],
                "completada": result[4]
            })
        print(tarea_list)
        return tarea_list
    
    @classmethod
    def get_tarea_by_id(cls, id_tarea):
        print(id_tarea)
        query = '''
        SELECT
            tarea.id_tarea,
            tarea.nombre,
            tarea.fecha_creacion,
            tarea.fecha_limite,
            tarea.completada,
            tarea.fk_categoria
        FROM
            tarea
        WHERE
            tarea.id_tarea = %s
        '''
        params = (id_tarea,)
        result = DatabaseConnection.fetch_one(query, params)
        
        
        if result is not None:
            return Tarea(
                id_tarea = result[0],
                nombre = result[1],
                fecha_creacion = result[2],
                fecha_limite = result[3],
                completada = result[4],
                id_categoria= result[5]
            )
        else:
            return None
        
    @classmethod
    def create_tarea(cls, tarea):
        query = '''
        INSERT INTO tarea (nombre, fecha_creacion, fecha_limite, completada,fk_categoria)
        VALUES (%s, %s, %s, %s ,%s)
        '''
        values = (tarea.nombre, tarea.fecha_creacion, tarea.fecha_limite, tarea.completada ,tarea.id_categoria)
        
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True