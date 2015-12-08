__author__ = 'Rochish'

# limited_infection.py
from user import User, CoachingGraph
from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


nodeList = [User("joe", 3), User("john"), User("jimmy", 2), User("tim", 1), User("roch"),
            User("max", 0), User("ronald", 2), User("kim", 2)]

# takes in a graph and a user in that graph
# traverses the graph, infecting only certain users

def infect(graph, user):
    queue = Queue()
    queue.put(user)
    infected = []

    while not queue.empty():
        cur = queue.get()
        if cur not in infected:
            # only infect those with frequencies 2 or 3
            if cur.frequency >= 2:
                cur.setVersion(2)
                infected.append(cur)
                for n in graph.getNeighbors(cur):
                    queue.put(n)
    return infected

def drawGraph(graph):
    G = nx.Graph(type="limited")
    for node in graph.listUsers():
        G.add_node(node.name, version=node.version, frequency=node.getFrequency())

    for node in graph.listUsers():
        for neighbor in graph.getNeighbors(node):
            if not G.has_edge(node.name, neighbor.name):
                G.add_edge(node.name, neighbor.name)

    # sort all infected users into a dictionary entitled v2
    sorted = sortUsers(G)

    pos = nx.spring_layout(G)
    # infected users will be represented as blue nodes
    nx.draw_networkx_nodes(G,pos, sorted["v2"], node_color="b", node_size=800)
    # uninfected users will be represented as red nodes
    nx.draw_networkx_nodes(G, pos, sorted["v1"], node_color="r", node_size=800)
    nx.draw_networkx_edges(G, pos)


    nx.draw_networkx_labels(G, pos, font_size=16)

    plt.savefig("limited_infection.png")

def sortUsers(graph):
    v2 = nx.get_node_attributes(graph, "version")
    r = dict(v2) # shallow copy of v2
    v1 = {}

    # go through v2 and remove any keys representing users
    # that are uninfected and add them to the v1 dictionary
    for key, value in r.items():
        if value == 1:
            v1[key] = value
            v2.pop(key)
    return {"v1": v1, "v2": v2}


if __name__ == '__main__':
    # main method goes here
    graph = CoachingGraph(nodeList)

    # add edges to graph
    graph.addEdge(graph.getUserByName("kim"), graph.getUserByName("joe"))
    graph.addEdge(graph.getUserByName("joe"), graph.getUserByName("john"))
    graph.addEdge(graph.getUserByName("joe"), graph.getUserByName("ronald"))
    graph.addEdge(graph.getUserByName("ronald"), graph.getUserByName("max"))
    graph.addEdge(graph.getUserByName("kim"), graph.getUserByName("tim"))
    graph.addEdge(graph.getUserByName("jimmy"), graph.getUserByName("tim"))
    graph.addEdge(graph.getUserByName("tim"), graph.getUserByName("roch"))
    graph.addEdge(graph.getUserByName("ronald"), graph.getUserByName("jimmy"))

    # lets infect kim
    infected = infect(graph, graph.getUserByName("kim"))
    drawGraph(graph)
    for user in infected:
        print(user.name + " was infected!")
