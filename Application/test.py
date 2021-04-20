import csv

# Méthode permettant d'obtenir des informations
def get_data(time):
    with open('./data/data.csv') as test:
        reader = csv.reader(test, delimiter=',')
        if time == 0:
            return 0, 0
        else:
            brut_row = [row for id, row in enumerate(reader) if id in (time, time)]
            row = brut_row[0]
            return float(row[1]), float(row[2])