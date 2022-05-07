board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

x = "A3" 
row = ""
colum = ""

def get_row_col(x):
    for i in x:
        if i == "A":
            colum = 0
        if i == "B":
            colum = 1
        if  i == "C":
            colum = 2
        if i == "1":
            row = 0
        if i == "2":
            row = 1
        if i == "3":
            row = 2
    print((row,colum))     
    return (row,colum)   
 
        
    


get_row_col(x)