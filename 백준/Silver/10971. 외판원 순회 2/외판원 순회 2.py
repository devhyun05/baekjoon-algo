num_of_cities = int(input())
visited_cities = []

for _ in range(num_of_cities):
    visited_cities.append(list(map(int, input().split())))

visited = [False] * num_of_cities
answer = float('inf')

def backtrack(start_city, current_city, count, total_cost):
    global answer

    if count == num_of_cities:
        if visited_cities[current_city][start_city] != 0:
            answer = min(answer, total_cost + visited_cities[current_city][start_city])
        return

    for next_city in range(num_of_cities):
        if not visited[next_city] and visited_cities[current_city][next_city] != 0:
            visited[next_city] = True
            backtrack(start_city, next_city, count + 1, total_cost + visited_cities[current_city][next_city])
            visited[next_city] = False

for start in range(num_of_cities):
    visited[start] = True
    backtrack(start, start, 1, 0)
    visited[start] = False

print(answer)