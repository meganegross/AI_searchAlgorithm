from graphProblem import *

class BFS_graph_algorithm_for_graph:
    def __init__(self):
        self.algorithm_name = 'BFS_graph_for_graph'

    def __call__(self):
        print ('Algorithm: {}'.format(self.algorithm_name))
        return self.breadth_first_search_graph

    def breadth_first_search_graph_for_vis(self, problem):
        
        # we use these two variables at the time of visualisations
        iterations = 0
        all_node_colors = []
        node_colors = {k : 'white' for k in problem.graph.nodes()}
        
        node = Node(problem.initial)
        
        node_colors[node.state] = "red"
        iterations += 1
        all_node_colors.append(dict(node_colors))
          
        if problem.goal_test(node.state):
            node_colors[node.state] = "green"
            iterations += 1
            all_node_colors.append(dict(node_colors))
            return(iterations, all_node_colors, node)
        
        frontier = deque([node])
        
        # modify the color of frontier nodes to blue
        node_colors[node.state] = "orange"
        iterations += 1
        all_node_colors.append(dict(node_colors))
            
        explored = set()
        while frontier:
            node = frontier.popleft()
            node_colors[node.state] = "red"
            iterations += 1
            all_node_colors.append(dict(node_colors))
            
            explored.add(node.state)     
            
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    if problem.goal_test(child.state):
                        node_colors[child.state] = "green"
                        iterations += 1
                        all_node_colors.append(dict(node_colors))
                        return(iterations, all_node_colors, child)
                    frontier.append(child)

                    node_colors[child.state] = "orange"
                    iterations += 1
                    all_node_colors.append(dict(node_colors))
                        
            node_colors[node.state] = "gray"
            iterations += 1
            all_node_colors.append(dict(node_colors))
        return None

    def breadth_first_search_graph(self, problem):
        """Search the deepest nodes in the search tree first."""
        iterations, all_node_colors, node = self.breadth_first_search_graph_for_vis(problem)
        return(iterations, all_node_colors, node)
