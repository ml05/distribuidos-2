import subprocess

# Lista de archivos Python a ejecutar
archivos_python = ['./consumer/consumer_humedad.py',
                    './consumer/consumer_luminosidad.py',
                    './consumer/consumer_pH.py',
                    './consumer/consumer_temperatura.py',
                    './consumer/consumer_CO2.py']

# Lista para almacenar los procesos
procesos = []

# Ejecutar cada archivo Python en un proceso separado
for archivo in archivos_python:
    proceso = subprocess.Popen(['python', archivo])
    procesos.append(proceso)

# Esperar a que todos los procesos terminen
for proceso in procesos:
    proceso.wait()

print("Consumers corriendo")
