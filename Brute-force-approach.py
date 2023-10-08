import itertools

def calculate_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        city1 = points[order[i]]
        city2 = points[order[i + 1]]
        total_distance += calculate_distance_between_cities(city1, city2)
    return total_distance

def calculate_distance_between_cities(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def traveling_salesman_bruteforce(points):
    num_cities = len(points)
    if num_cities <= 2:
        return points

    # Generate all possible permutations of cities
    city_indices = list(range(num_cities))
    shortest_order = None
    shortest_distance = float('inf')

    for order in itertools.permutations(city_indices):
        distance = calculate_distance(points, order)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_order = order

    shortest_path = [points[i] for i in shortest_order] + [points[shortest_order[0]]]
    return shortest_path, shortest_distance

if __name__ == "__main__":
    # Input: List of (x, y) coordinates for cities
    cities = [(0, 0), (1, 2), (2, 4), (3, 1)]

    shortest_path, shortest_distance = traveling_salesman_bruteforce(cities)
    
    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
