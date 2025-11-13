import time
count = 0
def dls(graph, start, goal, limit):
    
    if start == goal:
        return [start]
    if limit <= 0:
        return None
    for neighbor in graph[start]:
        new_path = dls(graph, neighbor, goal, limit - 1)
        if new_path:
            return [start] + new_path
    return None

def iddfs(graph, start, goal, max_depth):
    global count
    count += 1
    for depth in range(max_depth + 1):
        path = dls(graph, start, goal, depth)
        if path:
            return path
    return None


# ---------- INPUT ----------
graph = {}
n = int(input("Enter number of nodes: "))
print("Enter node names:")
nodes = input().split()
for node in nodes:
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter each edge (u v):")
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter max depth limit: "))

# ---------- EXECUTION ----------
t1 = time.time()
path = iddfs(graph, start, goal, max_depth)
t2 = time.time()

if path:
    print(f"\n✅ IDDFS Path: {' -> '.join(path)}")
else:
    print("\n❌ No path found within depth limit!")

print(f"⏱ Execution Time: {t2 - t1:.6f} seconds")
print("🧮 Time Complexity: O(b^d)")
print("📦 Space Complexity: O(b*d)")
print(f"🔍 Nodes Explored: {count}")