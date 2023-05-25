import json

# Ruta del archivo de texto
archivo = "log-producer.txt"
salida = "out-producer.txt"

# Leer el archivo de texto
with open(archivo, "r") as file:
    lines = file.readlines()

resultados = []
for line in lines:
    # Extraer los datos de timestamp y el número final
    data, timestamp = line.split(" ")
    data = json.loads(data)
    numero_final = int(timestamp.strip())
    timestamp = int(data["timestamp"])
    # Guardar los resultados
    resultado = numero_final - timestamp
    resultados.append(resultado)

# Escribir los resultados en el archivo de texto de salida
with open(salida, "w") as file:
    for resultado in resultados:
        file.write(str(resultado) + "\n")
