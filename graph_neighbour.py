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
        self.vertices_count,self.edges_count=0,0

        try:
            plik = open("dag.txt")
            dane = plik.read().split("\n")
            temp_list=dane[0].split(' ')
            self.vertices_count,self.edges_count=int(temp_list[0]),int(temp_list[1])
            temp_list.clear()

            self.small_init()

            for i in range(1,len(dane)):
                temp_list=dane[i].split(" ")
                if temp_list[0].isdigit()==True:
                    first,second=int(temp_list[0]),int(temp_list[1])
                    self.macierz[first][second]=1
            plik.close()
        except FileNotFoundError:
            print("Najpierw podaj liczbe wierzcholkow:")
            self.vertices_count=self.input_digit()

            print("Teraz podaj liczbe krawedzi:")
            self.edges_count=self.input_digit()

            print("Nastepnie wprowadz krawedzie w postaci wierzcholek z ktorego krawedz wychodzi, a nastepnie do ktorego wchodzi np:")
            print("0 1\nOznacza 0 -> 1\nZapisane dane sa sygnalizowane poprzez OK, brak sygnalu oznacza bledny format, petle wlasna, badz przekroczenie zakresu")

            self.small_init()
            for i in range(0,self.edges_count):
                first,second=self.input_edge()
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
