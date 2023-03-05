def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            distance = distances[current] + graph[current][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append(neighbor)
    
    return distances

nodes = int(input())
graph = []
line = []
for i in range(nodes):
    for j in range(nodes):
        line.append(int(input))
    graph.append(line)
start = int(input)

print(dijkstra(graph, start))