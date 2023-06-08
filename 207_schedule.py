from collections import deque as dq

class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        class NodeStatus():
            NOT_SEEN = 0
            SEEN = 1
            CLEARED = 2

        def allClear(node_list, seen_list):
            for node in node_list:
                seen_status = seen_list[node]
                if seen_status == NodeStatus.NOT_SEEN or seen_status == NodeStatus.SEEN:
                    return False
            # else all cleared
            return True

        def getFirstNotSeen(seen_list):
            """ Returns the array index of the first item in seen_list
                that is equal to NOT_SEEN
            """
            for i, seen in enumerate(seen_list):
                if seen == NodeStatus.NOT_SEEN:
                    return i
            # else there are none that haven't been seen
            return None

        nodes = range(numCourses)
        # each node will be mapped to a list of nodes that they are adjacent to
        adjacency_dict = dict(zip(nodes, [ [] for i in range(numCourses)]))  
        for req in prerequisites:
            adjacency_dict[req[0]].append(req[1])
            

        # make an array to prevent using the same node twice in any given path
        seen_map = [NodeStatus.NOT_SEEN for i in range(numCourses)]
        trace_stack = dq()  # will be a stack of integers indicating nodes on the current path

        trace_stack.append(getFirstNotSeen(seen_map))

        while not allClear(nodes, seen_map):
            this_node = -1  # init
            if len(trace_stack) == 0:
                this_node = getFirstNotSeen(seen_map)
            else:
                this_node = trace_stack.pop()
            neighbors = adjacency_dict[this_node]

            # print("\n---------------------------")
            # print("this_node:", this_node)
            # print("trace_stack:", trace_stack)
            # print("adj_dict:", adjacency_dict)
            # print("---------------------------")

            seen_map[this_node] = NodeStatus.SEEN
            if len(neighbors) == 0:  # this_node is leaf
                seen_map[this_node] = NodeStatus.CLEARED
            elif allClear(neighbors, seen_map):  # no more neighbors to explore
                seen_map[this_node] = NodeStatus.CLEARED
            else:
                # append the current node back to the stack so that it is revisted
                # and able to be cleared after its neighbors have been inspected
                trace_stack.append(this_node)
                for neighbor in neighbors:
                    seen_status = seen_map[neighbor]
                    if seen_status == NodeStatus.SEEN:
                        return False  # cycle detected
                    elif seen_status == NodeStatus.NOT_SEEN:
                        trace_stack.append(neighbor)
        # end of while loop
        
        # if all nodes have been cleared without a detected cycle, then course plan is possible
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))