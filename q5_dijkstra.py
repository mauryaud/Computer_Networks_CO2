import heapq

graph = {
    "A": {"B": 1, "C": 10},
    "B": {"A": 1, "D": 10, "E": 1},
    "C": {"A": 10, "D": 1},
    "D": {"B": 10, "C": 1, "E": 10},
    "E": {"D": 10, "F": 100, "B": 1},
    "F": {"E": 100}
}

dist = {
    node: float("inf")
    for node in graph
}

previous = {
    node: None
    for node in graph
}

dist["A"] = 0

queue = [(0, "A")]

while queue:

    current_distance, u = heapq.heappop(queue)

    if current_distance > dist[u]:
        continue

    for v, weight in graph[u].items():

        new_distance = current_distance + weight

        if new_distance < dist[v]:

            dist[v] = new_distance
            previous[v] = u

            heapq.heappush(
                queue,
                (new_distance, v)
            )


print("SHORTEST PATHS FROM A")

for node in graph:

    path = []
    current = node

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    print(
        "A to", node,
        "Cost:", dist[node],
        "Path:", " -> ".join(path)
    )