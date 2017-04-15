import random

class dag(object):

    def generate(self,number_of_vertices,density):

        self.number_of_vertices=int(number_of_vertices)
        self.number_of_edges=round((self.number_of_vertices*
        (self.number_of_vertices-1))/2*int(density)/100)

        counter=0
        X=[]

        for i in range(1,self.number_of_vertices+1):
            for j in range(1,i):
                X.append([i,j])
                counter+=1

        for i in range(counter-self.number_of_edges):
            X.pop(random.randrange(len(X)))

        Y=[x for x in range(1,self.number_of_vertices+1)]
        random.shuffle(Y)

        for i in range(0,len(X)):
            X[i][0],X[i][1]=Y[X[i][0]-1],Y[X[i][1]-1]

        plik=open("dag.txt","w")

        plik.write("{} {}".format(self.number_of_vertices,self.number_of_edges))
        for i,j in X:
            plik.write("\n{} {}".format(i,j))

        plik.close()
