class Solution(object):
    def validTree(self, n, edges):
        if n == 0:
            return False

        adj = create_adj_list(edges)

        nodes = set(x for x in range(n))

        # traverse
        queue = [(None, 0)]
        visited = set()

        while queue:
            parent, node = queue.pop()
            visited.add(node)

            for child in adj[node]:
                if child == parent:
                    continue
                elif child in visited:
                    return False
                else:
                    queue.append((node, child))

        # check for leftovers
        if nodes - visited:
            return False

        return True

from collections import defaultdict

# return dictionary of children
def create_adj_list(edges):
    adj = defaultdict(lambda: [])

    for [start, end] in edges:
        adj[start] += [end]
        adj[end] += [start]

    return adj
