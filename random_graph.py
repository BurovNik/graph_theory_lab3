import igraph as ig
import random

def add_vertex_to_graph(G: ig.Graph, vert_neighbours_count :dict, k: int):
    vertex = choose_vertex_connect_to(vert_neighbours_count, k)
    G.add_vertex(label=str(G.vcount()))
    G.add_edge(vertex, G.vcount()-1)
    vert_neighbours_count[vertex] += 1
    vert_neighbours_count[G.vcount()-1] = 1


def choose_vertex_connect_to(vert_neighbours_count: dict, k: int) ->int:
    #print(vert_neighbours_count)
    d_i = [it**k for it in vert_neighbours_count.values()]
    alpha = 1 / sum(d_i)
    vert_prob = dict(zip(vert_neighbours_count.keys(), [(it**k)*alpha for it in vert_neighbours_count.values()]))
    #print(list(vert_prob.values()))
    #print(list(vert_prob.keys()))
    # тут происходит выбор индекса вершины
    vert_index = random.choices(list(vert_prob.keys()), weights= list(vert_prob.values()))
    #print(vert_index[0])
    return(vert_index[0])