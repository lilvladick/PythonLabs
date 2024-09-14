import math

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

for i in sites:
    distances[i] = {}
    for j in sites:
        if i != j:
            x1, y1 = sites[i]
            x2, y2 = sites[j]

            distance = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
            distances[i][j] = distance


print(distances)




