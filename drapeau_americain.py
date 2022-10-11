from turtle import *
#Les couleurs
rouge = '#C30C3E'
blanc = '#FFFFFF'
bleu = '#00204C'

#Les dimensions, avec les codes Wikipédia ainsi que la dédicace de fin
A = 400
B = 760
C = 216
D = 304
E = 21.6
F = 21.6
G = 25
H = 25
K = 24.8
L = 30.8

#Les définitions
def tracer_etoile() : #Étoiles
    fillcolor(blanc)
    color(blanc)
    begin_fill()
    setheading(90) #Changer l'orientation
    forward(K/2)
    right(162)
    for i in range(5):
        forward(8)
        left(72)
        forward(8)
        right(144)
    setheading(-90)
    forward(K/2)
    end_fill()

def rectange_rougeblanc():
    begin_fill() #Rectangle Rouge
    fillcolor(rouge)
    color(rouge)
    for i in range(2): #Réalisation d'un demi réctange, 2 fois, afin de réaliser un rectange entier (permet d'obtimiser le programme)
        forward(B)
        right(90)
        forward(L)
        right(90)
    end_fill()
    penup()
    right(90)
    forward(L*2)
    left(90)
    pendown()
    
def rectangle_bleu(): #Réalisation d'un demi réctange, 2 fois, afin de réaliser un rectange entier (permet d'obtimiser le programme)
    begin_fill() #Rectangle Bleu
    fillcolor(bleu)
    color(bleu)
    for i in range(2):
        forward(D)
        right(90)
        forward(C)
        right(90)
    end_fill()
    
#Début du programme
speed(100) #N'hésitez pas à augmenter la vitesse
penup()
setposition(-B/2, A/2) #Position de départ
pendown()

for i in range(7):
    rectange_rougeblanc() #Réaliser les 13 bandes
penup()
setposition(-380.00,199.60) #Position de départ pour le rectange bleu
pendown()
rectangle_bleu() #Réalisation du rectange bleu

setposition(-B/2, A/2) #Position de départ
for e in range(4): #Permet de mettre au milieu de la première étoiles
    penup()
    setheading(-90)
    forward(E)
    setheading(0)
    forward(H)
    pendown()
    for b in range(6): #Réalisation des lignes de 6 étoiles
        tracer_etoile()
        penup()
        setheading(0)
        if b < 5 :
            forward(2*G)
            pendown()
    setheading(-90)
    forward(E)
    setheading(180)
    forward(H)
    for c in range(5): #Réalisation des lignes de 5 étoiles
        tracer_etoile()
        penup()
        setheading(180)
        forward(H*2)
        pendown()
penup()
setheading(-90)
forward(E)
setheading(0)
forward(G)
pendown()
for b in range(6): #La dernière ligne d'étoiles
    tracer_etoile()
    penup()
    setheading(0)
    if b < 5 :
        forward(2*G)
        pendown()
penup()
hideturtle() #Cacher la tortue pour admirer le résultat final

#Fin de script
exitonclick()

