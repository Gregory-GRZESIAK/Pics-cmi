
class systemecentree():

    list_of_rayon= []
    list_of_indice = []
    list_of_distance = []
    list_of_matrice = []

    nb_dioptre = 2

    def __init__(self) -> None:
        pass


    def multiply_matrice_two_by_two(self, first, second):
        "Formule obtenue via le site https://geekflare.com/multiply-matrices-in-python/"
        result = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*second)] 
                for A_row in first]
        return result
    
    def get_matrice_translation(self, e, n):
        print(f"translation ! n : {n}")
        return [[1, e/n], [0, 1]]
    
    def get_matrice_refraction(self, n1, n2, R):
        print("refraction !")
        print(f"n1 : {n1}, n2: {n2}")
        if n1!=n2:
            return [[1, 0], [-(n2-n1)/R, 1]]
        else : 
            return [[1, 0], [-1/R, 1]]

    def start(self):
        for i in range(self.nb_dioptre):
            valeur = float(input("Veuillez indiquer la valeur de S{}C{} : ".format(i,i)))
            self.list_of_rayon.append(valeur)

        for i in range(self.nb_dioptre+1):
            valeur = float(input("Veuillez indiquer la valeur de n{} : ".format(i)))
            self.list_of_indice.append(valeur)

        for i in range(self.nb_dioptre-1):
            valeur = float(input("Veuillez indiquer la valeur de S{}S{} : ".format(i, i+1)))
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
        
    def calc_and_print_result(self):

        indice_before = self.list_of_indice[0]

        indice_after = self.list_of_indice[-1]
        
        self.matrice_transfert = self.list_of_matrice[0]
        self.fo = round(-indice_before/(-self.matrice_transfert[1][0]),2)
        self.fi = round(indice_after/(-self.matrice_transfert[1][0]),2)
        self.SHi = round(self.fi*(self.matrice_transfert[0][0]-1),2)
        self.EHo = round(self.fo*(self.matrice_transfert[1][1]-1),2)
        self.ENo = round(self.fo*(self.matrice_transfert[1][1]-(indice_after/indice_before)),2)
        self.SNi = round(self.fi*(self.matrice_transfert[0][0]-(indice_before/indice_after)),2)
        self.EFo = round(self.fo*self.matrice_transfert[1][1],2)
        self.SFi = round(self.fi*self.matrice_transfert[0][0],2)

        print("Matrice transfert : ")
        print(self.matrice_transfert[0])
        print(self.matrice_transfert[1])

        print("EHo : {},    ENo : {}".format(self.EHo,self.ENo))
        print("SHi : {},    SNi : {}".format(self.SHi,self.SNi))
        print("HoNo : {},     HiNi : {},   fo+fi={}".format(-self.EHo+self.ENo,-self.SHi+self.SNi,self.fo+self.fi))
        print("EFo : {},    SFi : {}".format(self.fo*self.matrice_transfert[1][1],self.fi*self.matrice_transfert[0][0]))

a = systemecentree()
a.start()
a.calc_and_print_result()