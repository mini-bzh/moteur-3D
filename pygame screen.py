import pygame
import espace_geometrique as geo
import affichage as af
import math
import os
import time

pygame.init()

win_size = (925,925)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("CUUUUUB")

pygame.mouse.set_visible(False)
Font=pygame.font.SysFont('', 45 )
 

done=False
cmpt = {"DG":0, "Clock":0, "TB":0, "z":10, "x":0, "pf":-100}
size = (30,30)
coef = (1,1)
time_2=time.time()
pygame.time.wait(10)
sensi = (math.pi)/50

# piti_cube = geo.cube((20,20,20),7,(0,0,0))
while not done:
    pygame.mouse.set_pos((win_size[0]/2,win_size[1]/2))
    time_1,time_2=time_2,time.time()
    orientation=sensi*cmpt["DG"]%(2*math.pi)
    
    cube = geo.cube((25+cmpt["x"],12,cmpt["z"]+0),10,(sensi*cmpt["DG"],sensi*cmpt["Clock"],sensi*cmpt["TB"]),(15,5,cmpt["pf"]))
    cube2 = geo.cube((25+cmpt["x"],12,cmpt["z"]+20),10,(sensi*cmpt["DG"],sensi*cmpt["Clock"],sensi*cmpt["TB"]),(15,5,cmpt["pf"]))
    cube3 = geo.cube((5+cmpt["x"],12,cmpt["z"]+0),10,(sensi*cmpt["DG"],sensi*cmpt["Clock"],sensi*cmpt["TB"]),(15,5,cmpt["pf"]))
    cube4 = geo.cube((5+cmpt["x"],12,cmpt["z"]+20),10,(sensi*cmpt["DG"],sensi*cmpt["Clock"],sensi*cmpt["TB"]),(15,5,cmpt["pf"]))
    matrice = af.affiche(cube.point_cote(["***","|||","^^","°°","~~","..."]),size)
    #matrice = af.affiche(cube.point_cube("##")+cube2.point_cube("##")+cube3.point_cube("##")+cube4.point_cube("##"),size)


    l = [[Font.render(matrice[y][x], False, (255,255,255), (0,0,0)) for x in range(size[0])] for y in range(size[1])]

    
    win.fill((0,0,0))
    for x in range(len(l)):
        for y in range(len(l[x])):
            if not matrice[y][x]==" ":
#             if True:
                win.blit(l[y][x], (x*30, y*30))
    win.blit(Font.render(str(int(1/(time_2-time_1)))+" FPS"+" "*5+"FOV:"+str(cmpt["pf"]), False, (255,255,255), (0,0,0)),(0,win_size[1]-20))
    pygame.display.update()
    

    for event in pygame.event.get():
        
#         print(event.type,event.dict)
        
        if event.type==768:
            if event.dict['unicode']=='x':
                done=True

        if event.type==771:
            
            if event.dict['text']=='p':
                cmpt["Clock"] +=1
            if event.dict['text']=='m':
                cmpt["Clock"] -=1
            if event.dict['text']=='n':
                cmpt["pf"] -=1
            if event.dict['text']=='b':
                cmpt["pf"] +=1

            if event.dict['text']=='z':
                cmpt["z"] -=math.cos(orientation)
                cmpt["x"] -=math.sin(orientation)
            if event.dict['text']=='s':
                cmpt["z"] +=math.cos(orientation)
                cmpt["x"] +=math.sin(orientation)
            if event.dict['text']=='d':
                cmpt["z"] +=math.sin(orientation)
                cmpt["x"] -=math.cos(orientation)
            if event.dict['text']=='q':
                cmpt["z"] -=math.sin(orientation)
                cmpt["x"] +=math.cos(orientation)
                
            
                
        if event.type==1024:
            if event.dict['rel'][0]<0:
                cmpt["DG"] +=1
            elif not event.dict['rel'][0]==0:
                cmpt["DG"] -=1
                
            if event.dict['rel'][1]<0:
                cmpt["TB"] -=1
            elif not event.dict['rel'][1]==0:
                cmpt["TB"] +=1
            
            

        
                
        if event.type==pygame.QUIT:
            done=True


#         pygame.time.wait(10)

pygame.quit()
