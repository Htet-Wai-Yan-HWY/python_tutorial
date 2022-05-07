chaa="test"
i=0
new_chaa=[]


def add_dots(chaa):
    for i in chaa:
        new_chaa.append(i+".")
        listToString(new_chaa)
        
def listToString(chaa):
    final=""
    for j in new_chaa:
        final+=j
    return final[:-1]

    

    

add_dots(chaa)
print(listToString(chaa ))
