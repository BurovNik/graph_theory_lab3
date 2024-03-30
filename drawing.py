import igraph as ig
import matplotlib.pyplot as plt

def draw_graph(G: ig.Graph):
    fig, ax = plt.subplots(figsize=(11, 11))  # создание окна для рисования
    ig.plot(G,  # отрисовка графа
            target=ax,
            layout="auto",  # print nodes in a line layout
            vertex_size=50,  # размер вершины
            vertex_color="purple",  # цвет вершин
            vertex_frame_width=4.0,  #
            vertex_frame_color="white",  # цвет фона
            # vertex_label=G.vs["label"],  # добавление подписей
            vertex_label_size=12.0,  # размер подписей вершин
            # edge_label=G.es["weight"]  # добавление ребер
            )
    plt.show()

def draw_hist():
    fig, ax = plt.subplots(figsize=(11, 11))
    plt.show()


def draw_dependencies(xaxis: list, yaxis: list):
    plt.plot
    for k in range(4):
        plt.plot(xaxis, yaxis[k], label= f"степень k = {k+1}")
    plt.legend(fontsize=12, loc='best')
    plt.show()


