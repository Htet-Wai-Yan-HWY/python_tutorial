from time import sleep
import os


helicopter1 = "  ____.........--=T=--.........______"
helicopter2 = "     .             |:|                 "
helicopter3 = "     .             |:|                 "
helicopter4 = """:-. //           /""""""-.             """
helicopter5 = """ '-._____..--""(""'''"()`---._         """
helicopter6 = """ /:   .._   ''  ":""""'[] |""`\\     """
helicopter7 = """ ': :'     `-.     :.     '"""" :    """
helicopter8 = """  ::          '--=:____:.___....-"     """
helicopter9 = """                    O"       O" grp    """

for i in range(1,200):
    if i < 39:
        print(helicopter1[-i:])
        print(helicopter2[-i:])
        print(helicopter3[-i:])
        print(helicopter4[-i:])
        print(helicopter5[-i:])
        print(helicopter6[-i:])
        print(helicopter7[-i:])
        print(helicopter8[-i:])
        print(helicopter9[-i:])
        sleep(0.1)
        os.system('clear')
    else:
        j = (int(i) - 39)
        print(str(" " * j) + helicopter1)
        print(str(" " * j) + helicopter2)
        print(str(" " * j) + helicopter3)
        print(str(" " * j) + helicopter4)
        print(str(" " * j) + helicopter5)
        print(str(" " * j) + helicopter6)
        print(str(" " * j) + helicopter7)
        print(str(" " * j) + helicopter8)
        print(str(" " * j) + helicopter9)
        sleep(0.1)
        os.system('clear')