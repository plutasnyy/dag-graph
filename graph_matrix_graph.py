from basic_class import basic_class
class graph_matrix(basic_class):
    def add_first_pointers(self,first,second):
        if self.matrix[first][self.vertices_count+1]==-1:
            self.matrix[first][self.vertices_count+1]=second
        if self.matrix[second][0]==-1:
            self.matrix[second][0]=first
        if self.matrix[0][second]==-1:
            self.matrix[0][second]=first
        if self.matrix[self.vertices_count+1][first]==-1:
            self.matrix[self.vertices_count+1][first]=second

    def add_in_matrix(self,first,second):
        self.add_first_pointers(first,second)

        self.matrix[first][second]=second+self.vertices_count#aktualizacja dla nastepnika
        pom=self.matrix[self.vertices_count+1][first]
        self.matrix[first][pom]=second+self.vertices_count

        self.matrix[second][first]=first
        pom=self.matrix[0][second]
        self.matrix[second][pom]=first

        self.matrix[0][second]=first#modyfikacja ostatnich wskaznikow
        self.matrix[self.vertices_count+1][first]=second

    def insert_minus_number(self):
        for i in range(1,self.vertices_count+1):
            X=[x for x in range(1,self.vertices_count+1) if self.matrix[i][x]<0 and x is not i]
            if len(X)>=1:
                self.matrix[i][i]=-1*X[0]
                pom=X[0]
                for j in range(1,len(X)):
                    self.matrix[i][pom]=-1*X[j]
                    pom=X[j]
                self.matrix[i][pom]=-1*pom
            else:
                self.matrix[i][i]=-1*i

    def small_init(self):
        ver=self.vertices_count+1
        for i in range(0,self.vertices_count+2):
            pom=[]
            for j in range(0,self.vertices_count+2):
                pom.append(-1)
            self.matrix.append(pom)


    def __init__(self):
        self.matrix=[]
        self.stack=[]

        input_data=self.read_data()
        self.vertices_count,self.edges_count=input_data[0]
        self.small_init()

        for i in range(1,len(input_data)):
            first,second=input_data[i]
            self.add_in_matrix(first,second)

        self.insert_minus_number()

    def print_edges(self):
        for i in range(0,self.vertices_count+2):
            pom=[]
            pom2=[""]
            for j in range(0,self.vertices_count+2):
                pom2.append(j)
                pom.append(self.matrix[i][j])
            if i == 0:
                print(pom2)
            print(i,",", pom)

    def in_level(self,i,indeks,visited_list):
        temp=self.matrix[i][indeks]
        if temp<=0 or temp==indeks:
            return 0
        else:
            return self.in_level(i,temp,visited_list)+1-(temp in visited_list)

    def vertices_degrees(self,visited_list=[]):
        tab=[]
        tab.append(-1)
        for i in range(1,self.vertices_count+1):
            tab.append(self.in_level(i,0,visited_list))
        for i in visited_list:
            tab[i]=-1
        return tab

    def DFS_sort(self,colors,vert=None,visited=[]):
        if  vert==None or colors[vert]=='szary':
            return False
        if colors[vert]=='czarny':
            return True
        colors[vert]='szary'
        visited.append(vert)
        count=self.vertices_count
        X=[x for x in range(1,count+1) if self.matrix[vert][x]>count]
        for i in X:
            if i is not vert:
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
