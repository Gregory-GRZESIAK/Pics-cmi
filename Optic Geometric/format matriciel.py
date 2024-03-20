import os
clear = lambda: os.system('cls')
clear()
class main():
    #value
    xe = [float, float]
    alphae = [float, float]
    dipotre_nb = int
    list_of_rayon = []
    list_of_indice = []
    list_of_distance = []
    void = " "
    stick = "|"
    droit = "-"
    end = ">"
    cross = "+"
    line = "-"
    epaisseur = 10
    hauteur = 3
    def __init__(self) -> None:
        self.main()
        pass
    def gen_image(self, dipotre_nb):
        j = 0
        output = []
        tempo2 = ""
        if self.list_of_rayon != []: #ligne pour voir la convergeance ou divergeance du dioptre
            for i in range(dipotre_nb):
                if self.list_of_rayon[i] >0:
                    rayon = "⸝"
                else :
                    rayon = "⸜"
                tempo2 += self.void*self.epaisseur + rayon
            output.append(tempo2)
            tempo2 = ""
        for i in range(dipotre_nb +1): #au dessus de l'axe optique avec les indices
            tempo = int((self.epaisseur-2)/2)*self.void + "n{}".format(i) + int(int(self.epaisseur-2)/2)*self.void + self.stick
            tempo2 += tempo
        tempo2 = tempo2.rstrip(tempo2[-1])
        output.append(tempo2)
        tempo2 = ""
        for i in range(self.hauteur) : # au dessus de l'axe optique
            for j in range(dipotre_nb):
                tempo2 += self.epaisseur*self.void + self.stick
            if i == self.hauteur-3:
                tempo2 += 2*self.epaisseur*self.void
                tempo2 = tempo2[:len(tempo2)-3] + self.cross + tempo2[len(tempo2)-2:]
            elif i == self.hauteur-2:
                tempo2 += 2*self.epaisseur*self.void
                tempo2 = tempo2[:len(tempo2)-4] + "-->" + tempo2[len(tempo2)-1:]
            output.append(tempo2)
            tempo2 = ""
        for i in range(dipotre_nb +1): # axe optique
            tempo = self.epaisseur*self.line + self.cross
            tempo2 += tempo
        tempo2 = tempo2.rstrip(tempo2[-1])
        tempo2 = tempo2[:4] + self.cross + tempo2[5:] + self.epaisseur*self.line + ">"
        tempo2 = tempo2[:len(tempo2)-6] + self.cross + tempo2[len(tempo2)-5:]
        output.append(tempo2)
        tempo2 = ""
        for i in range(dipotre_nb):# en dessous de l'axe optique avec les centre S
                tempo2 += int(self.epaisseur-2)*self.void + f"S{i}" + self.stick

        tempo2 = tempo2[:4] + "A" + tempo2[5:] + int(2*self.epaisseur+1)*self.void 
        tempo2 = tempo2[:len(tempo2)-6] + "A'" + tempo2[len(tempo2)-4:]
        output.append(tempo2)
        tempo2 = ""
        for i in range(self.hauteur) : #en dessous de l'axe optique
            for i in range(dipotre_nb):
                tempo2 += self.epaisseur*self.void + self.stick
            output.append(tempo2)
            tempo2 = ""
        if self.list_of_rayon != []:
            for i in range(dipotre_nb):
                if self.list_of_rayon[i] >0:
                    rayon = "⸜"
                else :
                    rayon = "⸝"
                tempo2 += self.void*self.epaisseur + rayon
            output.append(tempo2)
        for line in output:
            print(line)    
        

    def main(self):

        ask_nb_dioptre = int(input("Combien y'a t'il de dioptre ? -> "))
        print("Veuillez donc confirmer que votre représentation prend cette forme :" + "\n")
        self.gen_image(ask_nb_dioptre)
        
        for i in range(ask_nb_dioptre):
            valeur = int(input(f"Veuillez indiquer la valeur de S{i}C{i} : "))
            self.list_of_rayon.append(valeur)
        clear()
        self.gen_image(ask_nb_dioptre)

        for i in range(ask_nb_dioptre+1):
            valeur = float(input(f"Veuillez indiquer la valeur de n{i} : "))
            self.list_of_indice.append(valeur)
        self.dipotre_nb = ask_nb_dioptre

        valeur = float(input("Veuillez indiquer la distance AS0 (peut etre nulle) : "))
        self.list_of_distance.append(valeur)
        for i in range(ask_nb_dioptre):
            if i+1 != ask_nb_dioptre:
                valeur = float(input(f"Veuillez indiquer la distance S{i}S{i+1} (peut etre nulle) : "))
                self.list_of_distance.append(valeur)
            else : 
                valeur = float(input(f"Veuillez indiquer la distance S{i}A' (peut etre nulle) : "))
                self.list_of_distance.append(valeur)

        r = float(input("veuillez entrez la partie réelle de xe : "))
        i = float(input("veuillez entrez la partie immaginaire de xe : "))
        self.xe = [r,i]
        r = float(input("veuillez entrez la partie réelle de alphae : "))
        i = float(input("veuillez entrez la partie immaginaire de alphae : ")) 
        self.alphae = [r,i]
        xs = [float, float]
        nsalphas = [float, float]
        alphas  = [float, float]
        for i in range(ask_nb_dioptre*2+1):
            if i%2==0:
                result = self.translation(self.list_of_distance[int(i/2)], self.list_of_indice[int(i/2)], self.xe, self.alphae)
                xs = result[0][0]
                alphas[0] = result[1][0][0]/self.list_of_indice[int(i/2)]
                alphas[1] = result[1][0][1]/self.list_of_indice[int(i/2)]
                self.xe = xs
                self.alphae = alphas
            else : 
                result = self.refraction(self.list_of_rayon[int((i-1)/2)], self.list_of_distance[int((i-1)/2)], self.list_of_distance[int((i-1)/2)+1], self.xe, self.alphae)
                xs = result[0][0]
                alphas[0] = result[1][0][0]/self.list_of_indice[int((i-1)/2)+1]
                alphas[1] = result[1][0][1]/self.list_of_indice[int((i-1)/2)+1]
                self.xe = xs
                self.alphae = alphas
        print(xs)
        pass

    def translation(self, e:float, ne:float, xe:[float, float], alphae:[float, float]):
        
        ns_alphas : [float, float] = [ne*alphae[0], ne*alphae[1]] # ne = ns = n and alphae = alphas (in complex mode)

        xs = [float, float] # xs in complex mode
        xs = [xe[0]+ alphae[0]*e, xe[1]+ alphae[1]*e] #new value of xs

        matrice_sortie = [[xs],[ns_alphas]]# matrice 2*1
        print(f"translation !")
        return matrice_sortie

    def refraction(self, R:float, ne:float, ns:float, xe:[float, float], alphae:[float, float]):

        xs :[float, float] = xe # xs in complex mode

        ns_alphas :[float, float] = [ne*alphae[0]-((ns-ne)/R)*xe[0], ne*alphae[1]-((ns-ne)/R)*xe[1]] # in complex mode

        matrice_sortie = [[xs],[ns_alphas]] #matrice 2*1

        print(f"refraction !")
        return matrice_sortie


a = main()
