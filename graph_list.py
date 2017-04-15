from basic_class import basic_class
class graph_list(basic_class):
    def small_init(self,edges):
        for i in range(0,self.vertices_count+1):
            self.edges_list.append(["bialy"])
            edges.append([])#wypelnia tablice
    def write_to_list(self,edges):
        for i in range(1,self.vertices_count+1):
            self.edges_list[i].append(edges[i])

    def __init__(self):
        self.edges_list=[]
        self.stack=[]

        input_data=self.read_data()
        self.vertices_count,self.edges_count=input_data[0]

        edges=[]
        self.small_init(edges)

        for i in range(1,len(input_data)):
            a,b=input_data[i]
            edges[a].append(b)

        self.write_to_list(edges)

    def print_edges(self):
        for i in range(1,self.vertices_count+1):
            print(i,"->",self.edges_list[i])

    def vertices_degrees(self,visited_list=[]):
        tab=[]
        for i in range(0,self.vertices_count+1):
            tab.append(0)
        for i in range(1,self.vertices_count+1):
            if i in visited_list:
                tab[i]=-1
            else:
                for j in self.edges_list[i][1]:
                    if j not in visited_list:
                        tab[j]+=1
        tab[0]=-1
        return tab

    def DFS_sort(self,vert=None,visited=[]):
        if vert==None or self.edges_list[vert][0]=='szary':
            return False
        if self.edges_list[vert][0]=='czarny':
            return True
        self.edges_list[vert][0]='szary'
        visited.append(vert)
        for i in self.edges_list[vert][1]:
            if self.DFS_sort(i,visited)==False:
                return False;
        self.edges_list[vert][0]='czarny'
        self.stack.append(vert)
        return True;

    def dfs_sort(self):
        tab=self.vertices_degrees()
        pom=[x for x in range(1,len(tab)) if tab[x]==0]
        for i in pom:
            if self.DFS_sort(i)==False:
                print("Wykryto cykl")
        self.print_stack()

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
