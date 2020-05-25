import pygame
from pygame.locals import *
import random

class Node: 
    # Function to initialize the node object 
    def __init__(self,isStar,data,color): 
        self.coord = data  # Assign data(x,y coord)
        self.isStar=isStar
        self.color=color
        self.next = None  # Initialize next as null 
        self.enter= None
        self.exit = None
   
# Linked List class 
class LinkedList: 
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.coord) 
            temp = temp.next

if __name__=='__main__':
    pygame.init()

    width,height=512,700

    screen=pygame.display.set_mode((width,height))

    bg=pygame.image.load("resources/Board512x512.png")
    d1=pygame.image.load("resources/d1.jpg").convert()
    d2=pygame.image.load("resources/d2.jpg").convert()
    d3=pygame.image.load("resources/d3.jpg").convert()
    d4=pygame.image.load("resources/d4.jpg").convert()
    d5=pygame.image.load("resources/d5.jpg").convert()
    d6=pygame.image.load("resources/d6.jpg").convert()
    d1.set_alpha(128)
    d2.set_alpha(128)
    d3.set_alpha(128)
    d4.set_alpha(128)
    d5.set_alpha(128)
    d6.set_alpha(128)
    dicerollcoor=(350,556)
    
    btroll=pygame.image.load("resources/btRoll.png")
    btrollrec=pygame.Rect(btroll.get_rect())
    btrollcoor=(200,556)
    btrollrec.top=btrollcoor[1]
    btrollrec.left=btrollcoor[0]
    lastroll=-1

    setroll=False
    while 1:
        screen.fill(12)

        screen.blit(bg,(0,0))
        screen.blit(btroll,btrollcoor)

        if  setroll:
            tm=pygame.time.get_ticks()
            
            while pygame.time.get_ticks()<=tm+2000:
                tmn=(int)(pygame.time.get_ticks())
                if tmn%100==0:
                    num=random.randint(1,6)
                    lastroll=num
                    address="resources/d"+(str)(num)+".jpg"
                    dx=pygame.image.load(address)
                    screen.blit(dx,dicerollcoor)
                    pygame.display.flip()
            print(lastroll)
            setroll=False
        
        if lastroll>0 and lastroll<7:
            address="resources/d"+(str)(lastroll)+".jpg"
            dxt=pygame.image.load(address)
            screen.blit(dxt,dicerollcoor)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=event.pos
                if btrollrec.collidepoint(mouse_pos) and setroll==False:
                    setroll=True
