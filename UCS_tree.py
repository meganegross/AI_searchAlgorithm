from graphProblem import *

class UCS_tree_algorithm:

    def __init__(self):
        self.algorithm_name = 'UCS_tree'

    def __call__(self):
        print ('Algorithm: {}'.format(self.algorithm_name))
        return self.uniform_cost_search

    def best_first_graph_search(self, problem, f, display=False):
        """Search the nodes with the lowest f scores first.
        You specify the function f(node) that you want to minimize; for example,
        if f is a heuristic estimate to the goal, then we have greedy best
        first search; if f is node.depth then we have breadth-first search.
        There is a subtlety: the line "f = memoize(f, 'f')" means that the f
        values will be cached on the nodes as they are computed. So after doing
        a best first search you can examine the f values of the path returned."""
        f = memoize(f, 'f')
        iterations = 0
        node = Node(problem.initial)
        iterations += 1
        if problem.goal_test(node.state):
            iterations += 1
            return(iterations, node)
        frontier = PriorityQueue('min', f)
        iterations += 1
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            iterations += 1
            if problem.goal_test(node.state):
                iterations += 1
                if display:
                    print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
                return (iterations, node)
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    iterations += 1
                    frontier.append(child)
                elif child in frontier:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
            iterations += 1
        return None


    def uniform_cost_search(self, problem, display=False):
        return self.best_first_graph_search(problem, lambda node: node.path_cost, display)
