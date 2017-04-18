import sys
from graph_list import graph_list
from graph_neighbour import graph_neighbour
from graph_matrix_graph import graph_matrix
from generate_dag import dag

dag=dag()
dag.generate(10,20)

graph=graph_list()
graph.print_edges()
graph.dfs_sort()
graph.del_sort()
#print(graph.vertices_degrees())
#print("")

graph=graph_neighbour()
#graph.print_edges()
graph.dfs_sort()
graph.del_sort()
#print(graph.vertices_degrees())
#print("")

graph=graph_matrix()
#graph.print_edges()
graph.dfs_sort()
graph.del_sort()
#print(graph.vertices_degrees())
#print("")
