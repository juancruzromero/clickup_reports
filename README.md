<h1 align="center">
    Exportar datos de 
  <img align="center"; src="https://app.clickup.com/assets/images/brand/clickup-text.svg";>
</h1>

Script para exportar datos de ClickUP a excel y csv.

## 📋 Instalación:

1) Tener instalado Python.
2) Tener instalada las librerías pandas, openpyxl, PyYAML y requests*.
3) Indicar en el config.yaml el valor **"api_token"** se obtiene en https://app.clickup.com/settings/apps
4) Indicar en el config.yaml el/los valores de **"folder_ids"** (Estos indican las *"folders"* de los *"spaces"* de nuestra cuenta de ClickUp)
5) Ejecutar dentro de esta carpeta el comando : `python main.py`

\* Se recomienda el uso de un entorno virtual.

Una vez realizado estos pasos, se debería encontrar los archivos en esta carpeta a simple vista.

## 👩🏼‍💻 Modificar columnas del excel y csv:
Se puede sabiendo un poquito de python y manipulando el archivo **clean_tasks_dict.py** entre la línea 12 y 25.

## 😭 Posibles errores:
- Si no se exportan datos debe ser porque los valores **"api_token"** y/o **"folder_ids"** no estan bien.
- Porque no se utiliza la versión correcta de librerias especificadas en el requirements.txt.
- Proyecto realizado con Python 3.8.10
- Si encontras algo raro podes hacer pull request 😜.

## 🚀 Lista de mejoras
La comunidad **open-source** puede mantener este proyecto como desee. Algunas features que se podrían agregar:

- [ ] Almacenar en una base de datos.
- [ ] Hacer un dashboard de ejemplo.
- [ ] Deploy con Docker.

## 👫 Contribuidores
- [Juan Cruz Romero](https://github.com/juancruzromero)