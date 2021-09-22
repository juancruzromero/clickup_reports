from common import config
import pandas as pd
from datetime import datetime
from .clean_tasks_dict import CleanTasksDict

# CONSTANTES del config.yaml y class CleanTasksDict:
config_yaml = config()
CLEAN_TASKS_LIST = CleanTasksDict().get_clean_tasks_list()
FILE_NAME = config_yaml['file_name']
NOW = str(datetime.now().isoformat()).split(".")[0]

class ExportTasks():
    @staticmethod
    def export_tasks():
        """ Exporta a .xlsx y .csv con pandas
        con la lista CLEAN_TASKS_LIST.
        """
        print(" --- EXPORTANDO A XLSX Y CSV ---\n")
        df = pd.DataFrame.from_dict(CLEAN_TASKS_LIST)
        df.to_excel((FILE_NAME + NOW + ".xlsx"), index=False)
        print(" --- XLSX EXPORTADO ---\n")
        df.to_csv((FILE_NAME + NOW + ".csv"), index=False)
        print(" --- CSV EXPORTADO ---\n")