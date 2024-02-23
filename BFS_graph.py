from graphProblem import *

class BFS_graph_algorithm:
    def __init__(self):
        self.algorithm_name = 'BFS_graph'

    def __call__(self):
        print ('Algorithm: {}'.format(self.algorithm_name))
        return self.breadth_first_graph_search

    def breadth_first_graph_search(self, problem):
        """[Figure 3.11]
        Note that this function can be implemented in a
        single line as below:
        return graph_search(problem, FIFOQueue())
        """
        iterations = 0
        node = Node(problem.initial)
        iterations += 1
        if problem.goal_test(node.state):
            iterations += 1
            return(iterations, node)
        frontier = deque([node])
        iterations += 1
        explored = set()
        while frontier:
            node = frontier.popleft()
            iterations += 1
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    if problem.goal_test(child.state):
                        iterations += 1
                        return(iterations, child)
                    frontier.append(child)
                    iterations += 1
            iterations += 1
        return None
