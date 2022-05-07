import os
import time
index = 35
from time import sleep

file = open('test1.txt',mode='r',encoding='utf-8')




    #print(colum[1],end= "")
    #print(colum[2])
   # for i in range(0,35):
   #   helicopter=colum[i]
   #   print(helicopter,end="")
    
# def draw_heli():
#   for colum in file:
#     for i in range(0,index): 
#         print(colum[i],end="")
# draw_heli()    



def draw():
  for j in range(1,10):
    sp = str(" ") * j
    for i in file:
      print(str(sp) + i ,end="")
    sleep(1)
    os.system('clear')
    i = ""
    

draw()