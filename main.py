import sys
from graph_list import graph_list
from graph_neighbour import graph_neighbour

graph=graph_list()
graph.print_edges()
graph.dfs_sort()
graph.del_sort()

print("")

graph=graph_neighbour()
graph.print_edges()
