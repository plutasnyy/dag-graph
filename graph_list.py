class graph_list(object):

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
        self.vertices_count,self.edges_count=0,0

        try:
            plik = open("dag.txt")
            dane = plik.read().split("\n")
            temp_list=dane[0].split(' ')
            self.vertices_count,self.edges_count=int(temp_list[0]),int(temp_list[1])
            temp_list.clear()
            edges=[]
            self.small_init(edges)

            for i in range(1,len(dane)):
                temp_list=dane[i].split(" ")
                first,second=int(temp_list[0]),int(temp_list[1])
                edges[first].append(second)

            self.write_to_list(edges)
            plik.close()
        except FileNotFoundError:
            print("Najpierw podaj liczbe wierzcholkow:")
            self.vertices_count=self.input_digit()

            print("Teraz podaj liczbe krawedzi:")
            self.edges_count=self.input_digit()

            print("Nastepnie wprowadz krawedzie w postaci wierzcholek z ktorego krawedz wychodzi, a nastepnie do ktorego wchodzi np:")
            print("0 1\nOznacza 0 -> 1\nZapisane dane sa sygnalizowane poprzez OK, brak sygnalu oznacza bledny format, petle wlasna, badz przekroczenie zakresu")

            edges=[]
            self.small_init(edges)

            for i in range(0,self.edges_count):
                first,second=self.input_edge()
                edges[first].append(second)

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
        tab=self.vertices_degrees(visited)
        if vert==None:
            for i in tab:
                if i==0:
                    vert=i
                    break
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

    def print_stack(self):
        tab=[]
        while(len(self.stack)>0):
            tab.append(self.stack.pop())
        print(tab)

    def dfs_sort(self):
        tab=self.vertices_degrees()
        pom=[x for x in range(1,len(tab)) if tab[x]==0]
        for i in pom:
            if self.DFS_sort(i)==False:
                print("Wykryto cykl")
        self.print_stack()