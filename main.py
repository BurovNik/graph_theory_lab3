import igraph as ig
from drawing import draw_graph, draw_dependencies
from random_graph import add_vertex_to_graph

def main():
    avg_diameter = []
    it_count = 10
    max_vertex = 100

    for k in range(1, 5): # степень
        avg_diameter.append([])
        diameter = []
        for i in range((max_vertex - 1) // 5):
            diameter.append([])
        for i in range(it_count): # количество генераций дерева
            G = ig.Graph()
            G.add_vertices(2)
            G.vs["label"] = ["0", "1"]
            G.add_edge(0, 1)
            vert_neighbours_count = {0: 1, 1: 1}
            it = 0
            for ver_num in range(max_vertex - 2):  # количество вершин в дереве сейчас
                add_vertex_to_graph(G, vert_neighbours_count, k)
                if ver_num in range(5, max_vertex, 5):
                    diameter[it].append(G.diameter()) # тут должен быть вызов функции, считающей диаметр
                    it += 1
                if ver_num == 30 and i == 30:
                    draw_graph(G)
                    #print("12")
        for i in range((max_vertex-1) // 5):
            avg_diameter[k-1].append(sum(diameter[i])/len(diameter[i]))
    xaxis = []
    for i in range(5, max_vertex, 5):
        xaxis.append(i)
    draw_dependencies(xaxis, avg_diameter)
    #draw_graph(G)


main()
