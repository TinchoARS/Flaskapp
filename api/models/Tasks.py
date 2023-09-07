from ..database import DatabaseConnection
from flask import Flask, request, jsonify
from datetime import datetime

class tarea:
    def __init__(self, id_tarea, nombre, fecha_creacion, fecha_limite, completada, id_categoria):
       self.id_tarea = id_tarea
       self.nombre = nombre
       self.fecha_creacion = fecha_creacion
       self.fecha_limite = fecha_limite
       self.completada = completada
       self.categoria = id_categoria
       
    