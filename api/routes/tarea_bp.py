from flask import Blueprint
from ..controllers.task_controller import TareaController
from ..controllers.category_controller import CategoryController
from ..controllers.taskitem_controller import ItemController

tarea_bp = Blueprint('tarea_bp', __name__)
tarea_bp.route('/tareas', methods=['GET'])(TareaController.get_all_tasks)
tarea_bp.route('/tareas/<int:id_tarea>', methods=['GET'])(TareaController.get_task_by_id)
tarea_bp.route('/tareas', methods=['POST'])(TareaController.create_task)
tarea_bp.route('/categoria', methods=['POST'])(CategoryController.create_category)
tarea_bp.route('/item', methods=['POST'])(ItemController.create_item)
