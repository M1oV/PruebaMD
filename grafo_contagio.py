import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo_relaciones(relaciones, inicio, fin):
    """
    relaciones: lista de tuplas (trabajador_a, trabajador_b)
    inicio: trabajador origen
    fin: trabajador destino
    """
    G = nx.DiGraph()
    G.add_edges_from(relaciones)

    try:
        camino = nx.shortest_path(G, source=inicio, target=fin)
        print("Camino de conexión:", camino)
        aristas_camino = list(zip(camino, camino[1:]))
    except nx.NetworkXNoPath:
        print("No hay camino entre los trabajadores.")
        camino = []
        aristas_camino = []

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)

    if aristas_camino:
        nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color='red', width=2.5, arrows=True)

    plt.title("Relaciones de Contagio entre Trabajadores")
    plt.axis('off')
    plt.show()

# Ejemplo de uso:
if __name__ == "__main__":
    relaciones = [
        ('Trabajador1', 'Trabajador2'),
        ('Trabajador2', 'Trabajador3'),
        ('Trabajador3', 'Trabajador4'),
    ]
    visualizar_grafo_relaciones(relaciones, 'Trabajador1', 'Trabajador4')
