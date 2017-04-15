class basic_class(object):

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
                    if first<='0' or first>pom or second<='0' or second>pom or first==second:
                        first='a'
        print("OK")
        return int(first),int(second)

    def print_stack(self):
        tab=[]
        while(len(self.stack)>0):
            tab.append(self.stack.pop())
        print(tab)

    def read_data(self):

        edges_list=[]
        
        try:
            plik = open("dag.txt")
            dane = plik.read().split("\n")
            temp_list=[]
            for i in range(len(dane)):
                temp_list=dane[i].split(" ")
                if temp_list[0].isdigit()==True and temp_list[1].isdigit()==True:
                    first,second=int(temp_list[0]),int(temp_list[1])
                    edges_list.append([first,second])
            plik.close()

        except FileNotFoundError:
            print("Najpierw podaj liczbe wierzcholkow:")
            vertices_count=self.input_digit()

            print("Teraz podaj liczbe krawedzi:")
            edges_count=self.input_digit()

            edges_list.append([vertices_count,edges_count])
            print("Nastepnie wprowadz krawedzie w postaci wierzcholek z ktorego krawedz wychodzi, a nastepnie do ktorego wchodzi np:")
            print("1 3\nOznacza 1 -> 3\nZapisane dane sa sygnalizowane poprzez OK, brak sygnalu oznacza bledny format, petle wlasna, badz przekroczenie zakresu")

            for i in range(self.edges_count):
                first,second=self.input_edge()
                edges_list.append(first,second)

        return edges_list
