from basic_class import basic_class
class graph_matrix(basic_class):

    def small_init(self):

    def __init__(self):

    def print_edges(self):

    def vertices_degrees(self,visited_list=[]):

    def DFS_sort(self,colors,vert=None,visited=[]):

    def dfs_sort(self):

    def DEL_sort(self,visited=[]):
        tab=self.vertices_degrees(visited)
        pom=[x for x in range(1,len(tab)) if tab[x]==0]
        if len(pom)==0:
            return
        else:
            for i in pom:
                visited.append(i)
            self.DEL_sort(visited)

    def del_sort(self):
        tab=[]
        self.DEL_sort(tab)
        print(tab)
