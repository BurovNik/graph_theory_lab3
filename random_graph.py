import igraph as ig
import random

def add_vertex_to_graph(G: ig.Graph, vert_neighbours_count :dict):
    vertex = choose_vertex_connect_to(vert_neighbours_count)
    G.add_vertex()


def choose_vertex_connect_to(vert_neighbours_count: dict) ->int:
    print(vert_neighbours_count)
    alpha = 1 / sum(vert_neighbours_count.values())
    vert_prob = dict(zip(vert_neighbours_count.keys(), [it*alpha for it in vert_neighbours_count.values()]))
    print(list(vert_prob.values()))
    print(list(vert_prob.keys()))
    # тут происходит выбор индекса вершины
    vert_index = random.choices(list(vert_prob.keys()), weights= list(vert_prob.values()))
    print(vert_index)
    return(vert_index)