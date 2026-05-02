# a simple analysis of the data that I pull down from my cycling routes table
# author: Gerry Callaghan
# student number G00472971

from testing_downloading_from_API import readroutes

routes = readroutes()
total_elevation = 0
total_distance = 0
count = 0

for route in routes:
    total_elevation += routes[count]["elevation"]
    total_distance += routes[count]["distance"]
    print(total_elevation, total_distance)
    count = count + 1

print(f"The average elevation of the {count} routes is: {(total_elevation/count)} metres, while the average distance of the {count} routes is: {(total_distance/count)} kilometres,")





