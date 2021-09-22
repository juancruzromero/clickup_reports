from common import config
import requests

# CONSTANTES del config.yaml:
config_yaml = config()

API_URL = config_yaml['api_url']
FOLDER_PARAMS = config_yaml['folder_params']
SPRINT_PARAMS = config_yaml['sprint_params']        
FOLDER_IDS = config()['folder_ids']
HEADERS = {
    "Authorization": config()['api_token'],
    "Content-Type": "application/json"
}

class TasksDict():
    @staticmethod
    def get_tasks_dict():
        """Método que retorna la lista de tareas de
        lo/s folder_ids indicados en el config.yaml.

        Returns:
            dict: Diccionario con info de tareas dentro.
        """
        print("\n --- OBTENIENDO TAREAS DE CLICKUP ---\n")
        tasks = []

        folders_list = []
        for folder_id in FOLDER_IDS:
            uri = str(API_URL + FOLDER_PARAMS).format(folder_id)
            response = requests.get(uri, headers=HEADERS)
            if response.status_code == 200:
                response_dict = response.json()
                for element in response_dict['lists']:
                    folders_list.append(element['id'])
        
        for folder_list in folders_list:
            uri = uri = str(API_URL + SPRINT_PARAMS).format(folder_list)
            response = requests.get(uri, headers=HEADERS)
            response_dict = response.json()
            if response.status_code == 200:
                for task in response_dict['tasks']:
                    tasks.append(task)

        if tasks:
            print(" --- SE OBTUVIERON TAREAS ---\n")
        else:
            print(" --- NO SE OBTUVIERON TAREAS (REVISAR config.yaml)---\n")
        return tasks