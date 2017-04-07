class graph_matrix(object):

    def input_digit(self):
        value=input()
        while(value.isdigit()==False):
                print("Pamietaj aby wprowadzic cyfre:")
                value=input()
        return int(value)
    def input_edge(self):
        first,second="a a".split()
        while(first.isdigit()==False or second.isdigit()==False):
                dane=input().split()
                if(len(dane)==2):
                    first,second=dane[0],dane[1]
                    pom=str(self.vertices_count)
                    if first<'0' or first>pom or second<'0' or second>pom or first==second:
                        first='a'
        print("OK")
        return int(first),int(second)
    def small_init(self):

    def __init__(self):

    def print_edges(self):

    def vertices_degrees(self,visited_list=[]):

    def DFS_sort(self,colors,vert=None,visited=[]):

    def print_stack(self):
        tab=[]
        while(len(self.stack)>0):
            tab.append(self.stack.pop())
        print(tab)

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
