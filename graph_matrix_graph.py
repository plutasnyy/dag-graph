from basic_class import basic_class
class graph_matrix(basic_class):
    def add_in_matrix(self,first,second):
        pass

    def small_init(self):
        ver=self.vertices_count+1
        for i in range(0,self.vertices_count+2):
            pom=[]
            for j in range(0,self.vertices_count+2):
                pom.append(0)
            self.macierz.append(pom)
        self.macierz[0][0]=self.macierz[0][ver]=-1
        self.macierz[ver][0]=self.macierz[ver][ver]=-1


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
                if temp_list[0].isdigit()==True and temp_list[1].isdigit()==True:
                    first,second=int(temp_list[0]),int(temp_list[1])
                    self.add_in_matrix(first,second)
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
                self.add_in_matrix(first,second)

    def print_edges(self):
        for i in range(0,self.vertices_count+2):
            pom=[]
            pom2=[""]
            for j in range(0,self.vertices_count+2):
                pom2.append(j)
                pom.append(self.macierz[i][j])
            if i == 0:
                print(pom2)
            print(i,",", pom)

#    def vertices_degrees(self,visited_list=[]):

#    def DFS_sort(self,colors,vert=None,visited=[]):

#    def dfs_sort(self):

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
