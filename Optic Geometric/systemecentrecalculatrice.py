
class systemecentree():

    list_of_rayon= []
    list_of_indice = []
    list_of_distance = []
    list_of_matrice = []

    nb_dioptre = int(input("Nombre de dioptre : "))

    def __init__(self) -> None:
        pass
    
    def multiply_matrice_two_by_two(self, first, second):
        "Formule obtenue via le site https://geekflare.com/multiply-matrices-in-python/"
        result = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*second)] 
                for A_row in first]
        return result
    
    def get_matrice_translation(self, e, n):

        return [[1, e/n], [0, 1]]
    
    def get_matrice_refraction(self, n1, n2, R):
        if R!=0:
            if n1!=n2:
                return [[1, 0], [-(n2-n1)/R, 1]]
            else : 
                return [[1, 0], [-1/R, 1]]
        else: 
            return[[1,0],[0,1]]

    def start(self):
        for i in range(self.nb_dioptre):
            valeur = float(input("f{}/S{}C{} : ".format(i,i, i)))
            self.list_of_rayon.append(valeur)

        for i in range(self.nb_dioptre+1):
            valeur = float(input("n{} : ".format(i)))
            self.list_of_indice.append(valeur)

        for i in range(self.nb_dioptre-1):
            valeur = float(input("S{}S{} : ".format(i, i+1)))
            self.list_of_distance.append(valeur)

        for i in range(self.nb_dioptre*2-1):
            if i%2!=0:
                result = self.get_matrice_translation(self.list_of_distance[int(i/2)], self.list_of_indice[int(i/2)+1])
                
            else : 
                result =self.get_matrice_refraction(self.list_of_indice[int(i/2)], self.list_of_indice[int(i/2)+1], self.list_of_rayon[int((i)/2)])
            self.list_of_matrice.append(result)
        self.list_of_matrice.reverse()
        tempo = 0
        for i in range(len(self.list_of_matrice)-1):
            self.list_of_matrice[0] = self.multiply_matrice_two_by_two(self.list_of_matrice[0], self.list_of_matrice[i+1])
        
        for i in range(len(self.list_of_matrice[0])):
            for j in range(len(self.list_of_matrice[0][i])):
                self.list_of_matrice[0][i][j] = round(self.list_of_matrice[0][i][j],3)
             
    def calc_and_print_result(self):

        indice_before = self.list_of_indice[0]

        indice_after = self.list_of_indice[-1]
        
        self.matrice_transfert = self.list_of_matrice[0]
        self.fo = -indice_before/(-self.matrice_transfert[1][0])
        self.fi = indice_after/(-self.matrice_transfert[1][0])
        self.SHi = self.fi*(self.matrice_transfert[0][0]-1)
        self.EHo = self.fo*(self.matrice_transfert[1][1]-1)
        self.ENo = self.fo*(self.matrice_transfert[1][1]-(indice_after/indice_before))
        self.SNi = self.fi*(self.matrice_transfert[0][0]-(indice_before/indice_after))
        self.EFo = self.fo*self.matrice_transfert[1][1]
        self.SFi = self.fi*self.matrice_transfert[0][0]


        print("")
        print("Matrice transfert : ")
        print(self.matrice_transfert[0])
        print(self.matrice_transfert[1])
        print('fo : {}'.format(round(self.fo, 3)))
        print('fi : {}'.format(round(self.fi, 3)))
        print("EHo : {}".format(round(self.EHo, 3)))
        print("ENo : {}".format(round(self.ENo, 3)))
        print("SHi : {}".format(round(self.SHi, 3)))
        print("SNi : {}".format(round(self.SNi, 3)))
        print("HoNo : {},     HiNi : {},   fo+fi={}".format(round(-self.EHo+self.ENo, 3),round(-self.SHi+self.SNi, 3),round(self.fo+self.fi, 3)))
        print("EFo : {}".format(round(self.EFo, 3)))
        print("SFi : {}".format(round(self.SFi, 3)))

        tempo = True
        while tempo :
            suite = input("Souhaitez vous utiliser un point objet ? y/n (1/0) -> ")
            if suite == "y" or suite =="1":
                tempo = False
                self.calc_and_print_image()
            elif suite == "n" or suite =="0":
                tempo = False
                print("non")
            else : 
                print("Entre une valeur correcte")
    
    def calc_and_print_image(self):
        self.EAo = float(input("Quel est la distance EAo ? : "))

        self.po = - self.EHo + self.EAo
        self.pi = (self.po*self.list_of_indice[-1])/(-self.matrice_transfert[1][0]*self.po+self.list_of_indice[0])
        self.Gt = self.pi/self.po

        # T(HiAi) T(HoHi) T(AoHo)
        self.list_of_matrice_2 = [[[1, self.pi],[0, 1]],[[1,0],[self.matrice_transfert[1][0], 1]],[[1, -self.po],[0, 1]]]
        for i in range(len(self.list_of_matrice_2)-1):
            self.list_of_matrice_2[0] = self.multiply_matrice_two_by_two(self.list_of_matrice_2[0], self.list_of_matrice_2[i+1])
        self.Matrice_AoAi = self.list_of_matrice_2[0]

        for i in range(len(self.Matrice_AoAi)):
            for j in range(len(self.Matrice_AoAi)):
                self.Matrice_AoAi[i][j] = round(self.Matrice_AoAi[i][j],3)

        print("-------------------------------")
        print("po : {},  pi : {}".format(round(self.po,3), round(self.pi,3)))
        print("Gt (pi/po): {}".format(round(self.Gt,3)))
        print("Matrice AoAi : ")
        print(self.Matrice_AoAi[0])
        print(self.Matrice_AoAi[1])
a = systemecentree()
a.start()
a.calc_and_print_result()