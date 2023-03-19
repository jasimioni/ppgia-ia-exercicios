#!/usr/bin/env python3

import json
import argparse

def path_finder(target_city=None, start_city=None, straight_line_values=None, neighbors=None, debug=True):
    """
    target_city: string
    start_city: strinc
    straight_line_values: dictionary, each key is a source city and the value the distance to target_city
    neighbors: dictionary, each key a city and each value a dictionary with the destination city directly connected and the cost
        neighbors = {
            'Arad' : {
                'Bucharest' : 10
            },
            'Bucharest' : {
                'Arda' : 10,
                'Sibiu' : 20
            }
        }
    """

    # Set the first option as the starting city
    # For each option, carry the path_cost and have
    # a total_cost with path_cost + straight_line (to be sorted)
    options = [{
        'city' : start_city, 
        'path_cost' : 0,
        'total_cost' : straight_line_values[start_city],
        'path' : []
    }]

    # Avoiding loops
    visited = { start_city : True }

    # Avoiding some deep loop
    max_tries = 200
    while max_tries:
        if debug:
            print("Current options")
            print(json.dumps(options, indent=2))

        attempt = options.pop(0)

        if debug:
            print(f"Popped {attempt['city']}\n")

        if attempt['city'] == target_city:
            print(f"Chegamos ao destino com custo {attempt['path_cost']} e caminho {attempt['path']} -> {attempt['city']}")
            break
        else:
            for neighbor in neighbors[attempt['city']]:
                # Let's make sure we don't keep trying the same city
                if neighbor in visited:
                    continue
                visited[neighbor] = True
                options.append({
                    'city' : neighbor,
                    'path_cost' : attempt['path_cost'] + neighbors[attempt['city']][neighbor],
                    'total_cost' : attempt['path_cost'] + neighbors[attempt['city']][neighbor] + straight_line_values[neighbor],
                    'path' : [ *attempt['path'], attempt['city'] ]
                })

        # Sort the options by total_cost
        options = sorted(options, key=lambda x:x['total_cost'])
        max_tries -= 1        


if __name__ == "__main__":
    cities = [ "Arad", "Bucharest", "Craiova", "Dobreta", "Eforie", "Fagaras", "Giurgiu", "Hirsova", "Iasi", "Lugoj", 
            "Mehadia", "Neamt", "Oradea", "Piattempti", "Rimnicu Vilcea", "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerind", ]

    straight_line_to_bucharest = [ 366, 0, 160, 242, 161, 178, 77, 151, 226, 244, 241, 234, 380, 98, 193, 253, 329, 80, 199, 374, ]

    distance_matrix = [
        [ 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 140, 118, None, None, 75 ],
        [ None, 0, None, None, None, 211, 90, None, None, None, None, None, None, 101, None, None, None, 85, None, None ],
        [ None, None, 0, 120, None, None, None, None, None, None, None, None, None, 138, 146, None, None, None, None, None ],
        [ None, None, 120, 0, None, None, None, None, None, None, 75, None, None, None, None, None, None, None, None, None ],
        [ None, None, None, None, 0, None, None, 86, None, None, None, None, None, None, None, None, None, None, None, None ],
        [ None, 211, None, None, None, 0, None, None, None, None, None, None, None, None, None, 99, None, None, None, None ],
        [ None, 90, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None ],
        [ None, None, None, None, 86, None, None, 0, None, None, None, None, None, None, None, None, None, 98, None, None ],
        [ None, None, None, None, None, None, None, None, 0, None, None, 87, None, None, None, None, None, None, 92, None ],
        [ None, None, None, None, None, None, None, None, None, 0, 70, None, None, None, None, None, 111, None, None, None ],
        [ None, None, None, 75, None, None, None, None, None, 70, 0, None, None, None, None, None, None, None, None, None ],
        [ None, None, None, None, None, None, None, None, 87, None, None, 0, None, None, None, None, None, None, None, None ],
        [ None, None, None, None, None, None, None, None, None, None, None, None, 0, None, None, 151, None, None, None, 71 ],
        [ None, 101, 138, None, None, None, None, None, None, None, None, None, None, 0, 97, None, None, None, None, None ],
        [ None, None, 146, None, None, None, None, None, None, None, None, None, None, 97, 0, 80, None, None, None, None ],
        [ 140, None, None, None, None, 99, None, None, None, None, None, None, 151, None, 80, 0, None, None, None, None ],
        [ 118, None, None, None, None, None, None, None, None, 111, None, None, None, None, None, None, 0, None, None, None ],
        [ None, 85, None, None, None, None, None, 98, None, None, None, None, None, None, None, None, None, 0, 142, None ],
        [ None, None, None, None, None, None, None, None, 92, None, None, None, None, None, None, None, None, 142, 0, None ],
        [ 75, None, None, None, None, None, None, None, None, None, None, None, 71, None, None, None, None, None, None, 0 ],
    ]

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--s_city",
        help="Source City"
    )

    parser.add_argument(
        "--list_cities",
        help="List Cities",
        action='store_true'
    )

    args = parser.parse_args()

    if args.list_cities:
        for city in cities:
            print(city)
        exit(0)

    if args.s_city is None:
        parser.print_help()
        exit(1)

    if args.s_city not in cities:
        print(f"I don't know any city named {args.s_city}")
        exit(1)

    start_city = args.s_city
    target_city = 'Bucharest'

    neighbors = {}
    sltd = {}

    # Convert our distance_matrix and our straight_line_array to a dict format
    for s, s_city in enumerate(cities):
        neighbors[s_city] = {}
        for d, d_city in enumerate(cities):
            if s != d and distance_matrix[s][d] is not None:
                neighbors[s_city][d_city] = distance_matrix[s][d]
        sltd[s_city] = straight_line_to_bucharest[s]

    print(json.dumps(neighbors, indent=2))
    print(json.dumps(sltd, indent=2))

    path_finder(start_city=start_city, target_city=target_city, straight_line_values=sltd, neighbors=neighbors)
