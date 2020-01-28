from time import sleep
from colorama import init, Fore, Style
from random import *


print ("Moin, herzlich willkommen zu MASTERMIND. \n"
       "Es geht darum die richtige Combination herraus zu finden!")
sleep(2)
print("Es gibt 6 Farben!\n"+
       Fore.RED + "Rot : 1\n"+
       Fore.BLUE + "Blau : 2\n"+
       Fore.GREEN + "Gruen : 3\n"+
       Fore.YELLOW + "Gelb : 4\n"+
       Fore.MAGENTA + "Magenta : 5\n"+
       Fore.CYAN + "Cyan : 6")
sleep(2)
print(Style.RESET_ALL + "Die Combination besteht aus 4 Moeglichkeiten. Aber Achtung! Farben koennen sich doppeln!!\n"
       "!Viel Spass!")
print( "Bist du Bereit?(Du hast 8 Versuche)\n"
       "[Dann druecke Enter!]")
enter = raw_input()
Code = []
for i in range(0,4,1):
       Code.append(randint(1,6))
print ("Nun gebe den ersten Code an ( Vier Zahlen hintereinander!)")
print Code
richtigPos = 0
richtigCol = 0
for runde in range(0,7,1):
       eingaben = raw_input()
       eingabeList = []
       if len(eingaben) == 4:
              for i in eingaben:
                     eingabeList.append(int(i))
              print eingabeList
       else:
              print ("ICH SAGTE VIER!\n"
                     "Zur Strafe musst du von vorne Anfangen;)")
              break


       for e in eingabeList:
              for c in Code:
                     if e == c:
                            richtigCol = richtigCol + 1
                            break
       for r in range(0,4,1):
              for e in eingabeList:
                            if Code[r] == e:
                                   richtigPos = richtigPos + 1
                                   break

       print (str(richtigCol) + " waren von der Farbe her richtig und so viel waren komplett richtig: " + str(richtigPos) + "\nWeiter gehts..")
       richtigCol = 0
       richtigPos = 0



