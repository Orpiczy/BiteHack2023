office_graph_dict = {0: [1, 3],
                     1: [0, 2, 4],
                     2: [1, 5],
                     3: [0, 4, 6],
                     4: [1, 3, 5, 7],
                     5: [2, 4, 8],
                     6: [3, 7],
                     7: [4, 6, 8],
                     8: [5, 7]}

vertices_nb = 9
weighted_graph = [[]]*vertices_nb

for vertice, edges in office_graph_dict.items():
    weighted_graph[vertice] = [int(i in edges) for i in range(vertices_nb)]

for edges in weighted_graph:
    print(edges)


def dijktra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    # Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if(i == source):
            shortest[source] = 0  # graph[source][source]
        else:
            if(graph[source][i] == 0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i

    if(source == dest):
        return 0
    # Dijktra's in Play
    selected.append(ind)
    while(ind != dest):
        # print('ind',ind)
        for i in range(l):
            if i not in selected:
                if(graph[ind][i] != 0):
                    # Check if distance needs to be updated
                    if((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000
        # print('shortest:',shortest)
        # print('selected:',selected)

        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)

    return shortest[dest]

# Finding odd degree vertices in graph


def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if(graph[i][j] != 0):
                degrees[i] += 1

    # print(degrees)
    odds = [i for i in range(len(degrees)) if degrees[i] % 2 != 0]
    print('odds are:', odds)
    return odds

# Take Odd Vertices from odds list and get all pairs in column wise fashion as shown in previous figures


def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1, len(odds)):
            pairs[i].append([odds[i], odds[j]])

    print('pairs are:', pairs)
    # print('\n')
    return pairs


pairs = gen_pairs(odds)
l = (len(pairs)+1)//2

pairings_sum = []


def get_pairs(pairs, done=[], final=[]):
    if(pairs[0][0][0] not in done):
        done.append(pairs[0][0][0])

        for i in pairs[0]:
            f = final[:]
            val = done[:]
            if(i[1] not in val):
                f.append(i)
            else:
                continue

            if(len(f) == l):
                pairings_sum.append(f)
                return
            else:
                val.append(i[1])
                get_pairs(pairs[1:], val, f)

    else:
        get_pairs(pairs[1:], done, final)


get_pairs(pairs)
print('pairings_sum', pairings_sum)


print(get_odd(weighted_graph))
