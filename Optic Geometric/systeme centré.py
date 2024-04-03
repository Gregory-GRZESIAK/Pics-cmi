def multiply_matrice_two_by_two(first, second):
    "Formule obtenue via le site https://geekflare.com/multiply-matrices-in-python/"
    result = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*second)] 
            for A_row in first]
    return result
def get_matrice_translation(e,n):
    return [[1, e/n], [0, 1]]
def get_matrice_refraction(n1, n2, R):
    if n1!=n2:
        return [[1, 0], [-(n2-n1)/R, 1]]
    else : 
        return [[1, 0], [-1/R, 1]]
list_of_rayon= []
list_of_indice = []
list_of_distance = []
list_of_matrice = []

nb_dioptre = 2
for i in range(nb_dioptre):
    valeur = float(input(f"Veuillez indiquer la valeur de S{i}C{i} : "))
    list_of_rayon.append(valeur)

for i in range(nb_dioptre+1):
    valeur = float(input(f"Veuillez indiquer la valeur de n{i} : "))
    list_of_indice.append(valeur)

for i in range(nb_dioptre-1):
    valeur = float(input(f"Veuillez indiquer la valeur de S{i}S{i+1} : "))
    list_of_distance.append(valeur)

for i in range(nb_dioptre*2-1):
    if i%2!=0:
        result = get_matrice_translation(list_of_distance[int(i/2)], list_of_indice[int(i/2)])
        
    else : 
        result =get_matrice_refraction(list_of_indice[i-1], list_of_indice[i], list_of_rayon[int((i)/2)])
    list_of_matrice.append(result)
list_of_matrice.reverse()
tempo = 0
for i in range(len(list_of_matrice)-1):
    list_of_matrice[0] = multiply_matrice_two_by_two(list_of_matrice[0], list_of_matrice[i+1])
    
indice_before = list_of_indice[0]

indice_after = list_of_indice[-1]
matrice_transfert = list_of_matrice[0]
fo = round(-indice_before/(-matrice_transfert[1][0]),2)
fi = round(indice_after/(-matrice_transfert[1][0]),2)
SHi = round(fi*(matrice_transfert[0][0]-1),2)
EHo = round(fo*(matrice_transfert[1][1]-1),2)
ENo = round(fo*(matrice_transfert[1][1]-(indice_after/indice_before)),2)
SNi = round(fi*(matrice_transfert[0][0]-(indice_before/indice_after)),2)
EFo = round(fo*matrice_transfert[1][1],2)
SFi = round(fi*matrice_transfert[0][0],2)

print("Matrice transfert : ")
print(matrice_transfert[0])
print(matrice_transfert[1])

print(f"EHo : {EHo},    ENo : {ENo}")
print(f"SHi : {SHi},    SNi : {SNi}")
print(f"HoNo : {-EHo+ENo},     HiNi : {-SHi+SNi},   fo+fi={fo+fi}")
print(f"EFo : {fo*matrice_transfert[1][1]},    SFi : {fi*matrice_transfert[0][0]}")