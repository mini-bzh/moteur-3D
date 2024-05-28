

def affiche(liste_point,size,m = None):
    liste_point_xy = [i[0:2] for i in liste_point]
    matrice = [[" " for x in range(size[1])] for y in range(size[0])]
    
    for y in range(size[1]):
        for x in range (size[0]):
            if (x,y) in liste_point_xy:
                point = list()
                
                for i in liste_point:
#                     if not len(i)==4:
#                             print(i)
                    if i[0:2] == (x,y) and i[2]>-10 or i[0:2] == [x,y] and i[2]>10:
                        point.append(i)
                
                if point != list():
                    z_mini = 0
                    cle_z_mini = 0
                    
                    for i in range(len(point)):
                        if point[i][2]<z_mini:
                            z_mini = point[i][2]
                            cle_z_mini = i
                    matrice[y][x] = point[cle_z_mini][3]
    return matrice


