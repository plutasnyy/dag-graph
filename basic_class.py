class basic_class(object):

    def input_digit(self):
        value=input()
        while(value.isdigit()==False):
                print("Pamietaj aby wprowadzic cyfre:")
                value=input()
        print("OK")
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
            print("Krawedzie prowadzaj parami wraz z odstepem spacji, np 1 2 oznacza krawedz skierowana 1->2")
            print("Zaakceptowanie danych jest sygnalizowane przez OK, brak sygnalu oznacza blad")
            print("Zacznij od wprowadzenia liczby wierzcholkow, a potem krawedzi. POJEDYNCZO")

            self.vertices_count=self.input_digit()
            self.edges_count=self.input_digit()
            edges_list.append([self.vertices_count,self.edges_count])

            for i in range(self.edges_count):
                first,second=self.input_edge()
                edges_list.append([first,second])

            plik=open("dag.txt","w")

            for i,j in edges_list:
                plik.write("\n{} {}".format(i,j))

            plik.close()

        return edges_list
