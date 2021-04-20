import csv
import numpy as np

# Création des listes des coordonnées des points du circuit à partir du fichier csv
x_circuit, y_circuit = [], []

with open('./data/circuit.csv') as circuit:
    csv_reader = csv.reader(circuit, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count%2 == 0:
            x_circuit.append(row[0])
            y_circuit.append(row[1])
        line_count += 1

# Conversion des listes en objets numpy
x_circuit, y_circuit = np.array(x_circuit).astype(np.float), np.array(y_circuit).astype(np.float)

# Calcul des valeurs pour l'échelle de la visualisation sur l'application web
xcm = np.min(x_circuit) - 2000
xcM = np.max(x_circuit) + 2000
ycm = np.min(y_circuit) - 2000
ycM = np.max(y_circuit) + 2000