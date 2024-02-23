from heading_v3 import *  

def add_node(node):
	node_location = dict()
	for node, location in node:
		node_location[node] = location
	return node_location

def add_neighbour(node_neighbour):
	neighbour = dict()
	for node in node_neighbour:
		node_name = node[0]
		if node_name in neighbour.keys():
			pass
		else:
			neighbour[node_name] = dict()
		for adjecent_node in node[1]:
			connected_node, distance = adjecent_node[0], adjecent_node[1]
			neighbour[node_name][connected_node] = distance
	return neighbour

def del_node(node, del_node_name):
    del node[del_node_name]

def def_neighbour(node_connnection, del_node_name):
    del node_connnection[del_node_name]

def define_graph(neighbour = None, location = None, use_romina = False):
    if use_romina:
        location = add_node(location)
        neighbour = add_neighbour(neighbour)
    graph = UndirectedGraph(neighbour)
    graph.locations = location
    node_colors = {node: 'white' for node in graph.locations.keys()}
    node_positions = graph.locations
    position_v = [x[1] for k, x in graph.locations.items()]
    max_v = max(position_v)
    node_label_pos = { k:[v[0],v[1]-10*(max_v/500.)]  for k,v in graph.locations.items() }
    edge_weights = {(k, k2) : v2 for k, v in graph.graph_dict.items() for k2, v2 in v.items()}

    graph_data = {  'graph_dict' : graph.graph_dict,
                            'node_colors': node_colors,
                            'node_positions': node_positions,
                            'node_label_positions': node_label_pos,
                             'edge_weights': edge_weights
                         }
    return graph_data, graph
