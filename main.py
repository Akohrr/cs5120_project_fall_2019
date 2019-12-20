import random
import time


def generate_edges(no_of_edges, node, vertices, graph):
    _edges = []
    options = vertices[:]
    for key, value in graph.items():
        if node in value:
            options.pop(options.index(key))

    while len(_edges) < no_of_edges:
        val = options[random.randint(0, len(options) - 1)]
        _edges.append(val)
        options.pop(options.index(val))
    edges = set(_edges)
    with open('generated_graph.txt', 'w+') as graph_writer:
        graph_writer.write(f'Edges of {node} is {edges}')
    return edges


def _generate_graph_helper(number_of_nodes, number_of_edges):
    vertices = [str(_) for _ in range(1, number_of_nodes+1)]
    graph = dict()
    for vert in vertices:
        graph[vert] = generate_edges(number_of_edges, vert, vertices, graph)
    return graph


def get_number_of_edges(__graph):
    no_of_nodes = 0
    no_of_edges = 0
    for key, values in __graph.items():
        no_of_edges += len(values)
        no_of_nodes += 1

    return no_of_nodes, no_of_edges


def bfs_min_path(graph, start_node, end_node):
    visited_path = []

    queue = [[start_node]]

    while len(queue) >= 1:
        _path = queue.pop(0)
        node = _path[-1]
        if node not in visited_path:
            children = graph[node]
            for child in children:
                path = list(_path)
                path.append(child)
                queue.append(path)
                if child == end_node:
                    return path

            visited_path.append(node)

    return None


def generate_graph(number_of_nodes, number_of_edges):
    generated_graph = None
    _pass = 0
    while _pass != 1:
        try:
            generated_graph = _generate_graph_helper(number_of_nodes, number_of_edges)
            _pass = 1
        except ValueError:
            continue

    size = get_number_of_edges(generated_graph)
    print(f"Total number of node in generated graph is {size[0]}, edges is {size[1]} ")
    return generated_graph


if __name__ == '__main__':
    random_number_for_filename = random.randint(0, 100)
    graphs_info_to_be_generated = {
        '1': {'nodes': 30, 'edges': 60},
        '2': {'nodes': 50, 'edges': 200},
        '3': {'nodes': 100, 'edges': 1000},
        '4': {'nodes': 200, 'edges': 4000},
    }

    for number, details in graphs_info_to_be_generated.items():
        print(f'Processing {number}, {details}')
        g = generate_graph(details["nodes"], details["edges"]//details["nodes"])
        with open(f'graph_data_{random_number_for_filename}.txt', 'a') as writer:
            writer.write(f"Graph {number} \n{{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in g.items()) + "}\n")
        _start = random.randint(1, details["nodes"])
        _end = random.randint(_start, details["nodes"])
        print(f"Start node is {_start}, end node is {_end}")
        start_time = time.time()
        shortest_path = bfs_min_path(g, str(_start), str(_end))
        end_time = time.time()
        time_taken = (end_time - start_time) * 1000  # time in milliseconds
        with open(f'output_data_{random_number_for_filename}.csv', 'a') as writer:
            writer.write(f"{shortest_path}, {time_taken}\n")

    print('Program completed successfully :).')
