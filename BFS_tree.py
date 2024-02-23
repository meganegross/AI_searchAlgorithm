from graphProblem import *

class BFS_tree_algorithm:
    def __init__(self):
        self.algorithm_name = 'BFS_tree'

    def __call__(self):
        print ('Algorithm: {}'.format(self.algorithm_name))
        return self.breadth_first_tree_search

    def breadth_first_tree_search(self, problem):
        """Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Don't worry about repeated paths to a state. [Figure 3.7]"""
        iterations = 0
        frontier = deque([Node(problem.initial)])  # FIFO queue
        iterations += 1
        while frontier:
            node = frontier.popleft()
            iterations += 1
            if problem.goal_test(node.state):
                iterations += 1
                return (iterations, node)
            frontier.extend(node.expand(problem))
            for n in node.expand(problem):
                iterations += 1
            iterations += 1
        return None