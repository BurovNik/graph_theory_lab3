import igraph as ig
from drawing import draw_graph, draw_dependencies
from random_graph import add_vertex_to_graph

def main():
    avg_diameter = []
    vert_neighbours_count = {}
    it_count = 500
    max_vertex = 100

    for k in range(1, 5): # степень
        avg_diameter.append([])
        diameter = []
        for i in range((max_vertex - 1) // 5):
            diameter.append([])
        for i in range(it_count): # количество генераций дерева
            G = ig.Graph()
            G.add_vertices(2)
            G.add_edge(0, 1)
            vert_neighbours_count[0] = 1
            vert_neighbours_count[1] = 1
            add_vertex_to_graph(G, vert_neighbours_count)
            it = 0
            for ver_num in range(max_vertex - 1):  # количество вершин в дереве сейчас
                if ver_num in range(5, max_vertex, 5):
                    diameter[it].append(ver_num) # тут должен быть вызов функции, считающей диаметр
                    it += 1
        for i in range((max_vertex-1) // 5):
            avg_diameter[k-1].append(sum(diameter[i])/len(diameter[i]))
    print(avg_diameter)
    xaxis = []
    for i in range(5, max_vertex, 5):
        xaxis.append(i)
    draw_dependencies(xaxis, avg_diameter)
    #draw_graph(G)


main()
