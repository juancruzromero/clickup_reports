from .tasks_dict import TasksDict

# CONSTANTE de class TasksDict:
TASKS_DICT = TasksDict().get_tasks_dict()

class CleanTasksDict():
    @staticmethod
    def get_clean_tasks_list():
        """Método que limpia la data cruda que viene
        directamente de ClickUp. De esta manera podemos
        crear reportes a nuestro antojo.

        Returns:
            list: Lista de tareas limpias.
        """
        print(" --- LIMPIANDO TAREAS ---\n")        
        clean_tasks_list = []

        for task in TASKS_DICT:
            task_dict = {
                "id": task.get("id"),
                "url": task.get("url"),
                "folder": task["folder"].get("name"),
                "list": task["list"].get("name"),
                "assignees": [human.get("username") for human in task.get("assignees")],
                "name": task.get("name"),
                "status": task["status"].get("status"),
                "start_date": task.get("start_date"),
                "due_date": task.get("due_date"),
                "time_spent" : task.get("time_spent")
            }
            clean_tasks_list.append(task_dict)
            print(f"Task: {task.get('name')}")
        
        print("\n --- TAREAS LIMPIAS ---\n")
        return clean_tasks_list