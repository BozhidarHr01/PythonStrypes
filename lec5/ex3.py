# имаме карта с магазини и разстояние между тях, искаме да 
# минем през всички за най-малко разстояние

store_map = { "Lidl" : {"Kaufland" : 10, "Technomarket" : 15},
              "Kaufland" : {"Lidl" : 10, "Technomarket" : 35},
              "Technomarket" : {"Lidl" : 15, "Kaufland" : 35}}

stores = ["Lidl", "Kaufland", "Technomarket"]

best_route = None
shortest_distance = 10000

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and i != k and j != k:
                route = [stores[i], stores[j], stores[k]]

                total = store_map[route[0]][route[1]] + store_map[route[1]][route[2]]

                print(f"{' -> '.join(route)}: {total}")

                if total < shortest_distance:
                    shortest_distance = total
                    best_route = route

print(f"Best route: {' -> '.join(best_route)}")
print(f"Total distance {shortest_distance}")