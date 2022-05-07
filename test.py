
import re


n = 1
list1 = [1,2,3]
list2 = [1,5,6]
real_list = sorted(list1 + list2)
y = len(real_list)

switch =  int()

def xdup(real_list):
    for i in range(0,y):
        if real_list[i] == real_list[i-1]:
            print ("1")
            switch == 1
            break
        else:
            print ("0")
            switch == 0
       


def list_xor(n,list1,list2):
    xdup(real_list)
    print (switch)
    # if switch == 0:
    #     for i in range(0,y):
    #         if real_list[i] == n:
    #             print ("True")
    #             return True
    #         else:
    #             print("False")
    #             return False
        
    
    # if switch == 1:
    #     print("False")
    #     return False


list_xor(n,list1,list2)
