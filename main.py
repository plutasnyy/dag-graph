import sys

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
        print("OK")
        return int(first),int(second)

    def small_init(self,edges):
        for i in range(0,self.vertices_count+1):
            self.edges_list.append(["bialy"])
            edges.append([])

    def write_to_list(self,edges):
        for i in range(1,self.vertices_count+1):
            self.edges_list[i].append(edges[i])

    def __init__(self):
        self.edges_list=[]
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
            print("0 1\nOznacza 0 -> 1\nZapisane dane sa sygnalizowane poprzez OK, brak sygnalu oznacza bledny format")

            edges=[]
            self.small_init(edges)

            for i in range(0,self.edges_count):
                first,second=self.input_edge()
                edges[first].append(second)

            self.write_to_list(edges)

    def print_edges(self):
        for i in range(1,self.vertices_count+1):
            print(i,"->",self.edges_list[i])

graph=graph_list()
graph.print_edges()
