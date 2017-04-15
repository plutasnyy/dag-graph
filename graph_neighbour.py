from basic_class import basic_class
class graph_neighbour(basic_class):
    def small_init(self):
        for i in range(0,self.vertices_count+1):
            pom=[]
            for j in range(0,self.vertices_count+1):
                if i==0 or j==0:
                    pom.append(-1)
                else:
                    pom.append(0)
            self.macierz.append(pom)

    def __init__(self):
        self.macierz=[]
        self.stack=[]

        input_data=self.read_data()
        self.vertices_count,self.edges_count=input_data[0]
        self.small_init()
        
        for i in range(1,len(input_data)):
            first,second=input_data[i]
            self.macierz[first][second]=1

    def print_edges(self):
        for i in range(1,self.vertices_count+1):
            pom=[]
            pom2=[""]
            for j in range(1,self.vertices_count+1):
                pom2.append(j)
                pom.append(self.macierz[i][j])
            if i == 1:
                print(pom2)
            print(i,",", pom)

    def vertices_degrees(self,visited_list=[]):
        tab=[]
        for i in range(0,self.vertices_count+1):
            tab.append(0)
        for i in range(1,self.vertices_count+1):
            if i in visited_list:
                tab[i]=-1
            else:
                pom=0
                for j in range(1,len(self.macierz[i])):
                    if j not in visited_list and self.macierz[i][j]:
                        tab[j]+=1
        tab[0]=-1
        return tab

    def DFS_sort(self,colors,vert=None,visited=[]):
        if  vert==None or colors[vert]=='szary':
            return False
        if colors[vert]=='czarny':
            return True
        colors[vert]='szary'
        visited.append(vert)
        for i in range(1,self.vertices_count+1):
            if self.macierz[vert][i]==1:
                if self.DFS_sort(colors,i,visited)==False:
                    return False;
        colors[vert]='czarny'
        self.stack.append(vert)
        return True;

    def dfs_sort(self):
        colors=[]
        for i in range(0,self.vertices_count+1):
            colors.append("bialy")
        tab=self.vertices_degrees()
        pom=[x for x in range(1,len(tab)) if tab[x]==0]
        for i in pom:
            if self.DFS_sort(colors,i,[])==False:
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
