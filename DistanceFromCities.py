dist_city_from_root = {}
adj_city = {}
def solution(T):
    length = len(T)
    visited = {}
    for i in range(length):
        adj_city[i] = T[i]
        dist_city_from_root[i] = 0
        visited[i] = False
        if i == T[i]:
            root = i

    find_adj_city(root, root, visited)

    result = [0 for i in range(length)]

    for i in range(length):
        result[dist_city_from_root[i]] += 1

    return result[1:]


def find_adj_city(Q, root, visited):
    for key in adj_city:
        if adj_city[key] == Q:
            if key != root and visited[key] == False:
                dist_city_from_root[key] = dist_city_from_root[Q] + 1
                visited[key] = True
                find_adj_city(key, root, visited)



T = [9,1,4,9,0,4,8,9,0 ,1]
x = solution(T)
print(x)
