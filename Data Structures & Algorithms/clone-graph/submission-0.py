"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Game Plan: 
        # oldToNew = dictionary containing nodes and their copies
        # visited = set of visited nodes
        # queue = holds the nodes that we are yet to traverse it's neighbors
        # then we iterate through all nodes in the stack until we have finished
        # traversing nodes and whilst we do that we will append the new nodes to queue
        # and while the queue is not empty we will pop a node and get it and traverse
        # its neighbors - adding the unvisited ones - 
        # once we are done exploring the graph
        # we will iterate through all key value pairs in the dictionary we have made and
        # take care of all required references between nodes and neighbors to represent the 
        # graph accurately
        if not node:
            return None 
            
        oldToNew = {}
        visited = set()
        q = deque()
        q.append(node)

        while q:
            n = q.popleft()
            newNode = Node(val = n.val)
            oldToNew[n] = newNode
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        for old, new in oldToNew.items():
            for neighbor in old.neighbors:
                new.neighbors.append(oldToNew[neighbor])

        return oldToNew[node]
