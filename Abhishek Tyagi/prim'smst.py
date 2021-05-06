

n, m = map(int, input().split())                
k = n + 1
nodes = list(range(k))                            
outside = [True] * k
dist = [200000] * k
conn = [{} for _ in range(k)]
for _ in range(m):
    x, y, r = map(int, input().split())
    conn[x][y] = conn[y][x] = min(r, conn[x].get(y, 200000))
res = dist[int(input())] = 0
for _ in range(n):                               
    nodes.sort(key=dist.__getitem__, reverse=True)
    curr = nodes.pop()
    outside[curr] = False
    res += dist[curr]
    for x, d in conn[curr].items():
        if outside[x] and dist[x] > d:
            dist[x] = d          
print(res)                                       

