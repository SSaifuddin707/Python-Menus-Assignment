import os, sys
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


item = ""
#os.system("cls")

                   
                            ###Sub Sub Menus###
    

def subMenu(finame):
    global data
    global result
    data = []
    result = None

    infile = open(finame, "r")
    infile.readline()
    for line in infile:
        line = line.strip("\n")
        result = tuple(line.split(","))
        data.append(result)
    infile.close()
    
def top5(num, name):
    sortD = sorted(data, key = lambda r:(float(r[num])), reverse = True)
    counter = 0
    print(color.BOLD + "Top 5 Players:\n" + color.END)
    for count in range(5):
        counter+=1
        print("{}. {}| Team: {}| {}: {}".format(counter, sortD[count][0], sortD[count][1],name, sortD[count][num]))
    input("\nPress Enter To Continue\n")
    os.system("cls")




                        ## QB Submenu Coding##
def QB():
    while True:
        OptionMenu("Option01Menu.txt")
        exite = input("\nWhat would you like to do?\n")
        if exite == "1":
            os.system("cls")
            subMenu("QB.txt")
            top5(3,"Completions")
     
        elif exite == "2":
            os.system("cls")
            subMenu("QB.txt")
            top5(4,"Attempts")

        elif exite == "3":
            os.system("cls")
            subMenu("QB.txt")
            top5(7,"Yards")

        elif exite == "4":
            os.system("cls")
            subMenu("QB.txt")
            top5(10,"Touchdowns")

        elif exite == "5":
            os.system("cls")
            subMenu("QB.txt")
            top5(11,"Interceptions")

        elif exite == str(tmpcount):
            os.system("cls")
            return    	
        else:
            leave = input("Wrong Input, press Enter to continue or type 'Exit' to end the program\n")
            if (leave == ""):
                os.system("cls")
                return
            elif (leave == "Exit") or (leave == "exit") or (leave == "EXIT"):
                sys.exit()

        
                        ##Running Backs##
def runBack():
    while True:

        OptionMenu("Option02Menu.txt")
        exite = input("\nWhat would you like to do?\n")
        if exite == "1":
            os.system("cls")
            subMenu("RB.txt")
            top5(3,"Attempts")

        elif exite == "2":
            os.system("cls")
            subMenu("RB.txt")
            top5(5,"Yards")

        elif exite == "3":
            os.system("cls")
            subMenu("RB.txt")
            top5(8,"Touchdowns")
            
        elif exite == "4":
            os.system("cls")
            subMenu("RB.txt")
            top5(9,"Longest")
            
        elif exite == "5":
            os.system("cls")
            subMenu("RB.txt")
            top5(10,"Fumbles")
            
        elif exite == str(tmpcount):
            os.system("cls")
            return
        else:
            leave = input("Wrong Input, press Enter to continue or type 'Exit' to end the program\n")
            if (leave == ""):
                os.system("cls")
                return
            elif (leave == "Exit") or (leave == "exit") or (leave == "EXIT"):
                sys.exit()    

                    ##Receivers##
def recVRS():
    while True:

        OptionMenu("Option03Menu.txt")
        exite = input("\nWhat would you like to do?\n")
        
        if exite == "1":
            os.system("cls")
            subMenu("RECV.txt")
            top5(3,"Receptions")
            
        elif exite == "2":
            os.system("cls")
            subMenu("RECV.txt")
            top5(4,"Yards")
            
        elif exite == "3":
            os.system("cls")
            subMenu("RECV.txt")
            top5(7,"Longest")
            
        elif exite == "4":
            os.system("cls")
            subMenu("RECV.txt")
            top5(8,"Touchdowns")
            
        elif exite == "5":
            os.system("cls")
            subMenu("RECV.txt")
            top5(9,"Fumbles")
            
        elif exite == str(tmpcount):
            os.system("cls")
            return
        else:
            leave = input("Wrong Input, press Enter to continue or type 'Exit' to end the program\n")
            if (leave == ""):
                os.system("cls")
                return
            elif (leave == "Exit") or (leave == "exit") or (leave == "EXIT"):
                sys.exit()

                        ##Tackles/Sacks##
def tACK():
    while True:

        OptionMenu("Option04Menu.txt")
        exite = input("\nWhat would you like to do?\n")
        
        if exite == "1":
            os.system("cls")
            subMenu("Tackles.txt")
            top5(4,"Tackles")
            
        elif exite == "2":
            os.system("cls")
            subMenu("Tackles.txt")
            top5(5,"Assisted")
            
        elif exite == "3":
            os.system("cls")
            subMenu("Sacks.txt")
            top5(6,"Sacks")
            
        elif exite == "4":
            os.system("cls")
            return         
        else:
            leave = input("Wrong Input, press Enter to continue or type 'Exit' to end the program\n")
            if (leave == ""):
                os.system("cls")
                return
            elif (leave == "Exit") or (leave == "exit") or (leave == "EXIT"):
                sys.exit()


                         ##Interceptions##
def INT():
    while True:

        OptionMenu("Option05Menu.txt")
        exite = input("\nWhat would you like to do?\n")
        
        if exite == "1":
            os.system("cls")
            subMenu("Interceptions.txt")
            top5(3,"Interceptions")

        elif exite == "2":
            os.system("cls")
            return         
        else:
            leave = input("Wrong Input, press Enter to continue or type 'Exit' to end the program\n")
            if (leave == ""):
                os.system("cls")
                return
            elif (leave == "Exit") or (leave == "exit") or (leave == "EXIT"):
                sys.exit()  

                         ##  All  Submenues  ##

def OptionMenu(fname):
    item = ""
    count = -1
    menu01 = open(fname, "r")
    for line in menu01:
        if line == "Back":
            tmpcount = count
            item += ("------------------------------\n{}. {}".format(count, line))
        elif count > 0:
            item += ("{}. {}".format(count, line))
        else:
            item += ("{}".format(line))
        count += 1
    
    print(item)
    menu01.close()

            ##Prints and processes Main Menu##

def main_menu():
    
    while True:
        #os.system("cls")
        print(item)
                        ##User Input##

        response = input("\nSelect an option [1-6]\n")

        ##Code for processing input from user##        
        if response == "1":	
            os.system("cls")
            QB()

        elif response == "2":
            os.system("cls")
            runBack()
            
            
        elif response == "3":
            os.system("cls")          
            recVRS()            

        elif response == "4":
            os.system("cls")
            tACK()
               
        elif response == "5":
            os.system("cls")
            INT()

        elif response == str(tmpcount):
            sys.exit()

        else:
            leave = input("Wrong Input, press Enter to continue or type 'Exit' to end the program\n")
            if (leave == ""):
                os.system("cls")
                main_menu()
            elif (leave == "Exit") or (leave == "exit") or (leave == "EXIT"):
                sys.exit()


               
                    ## Builds Main Menu ##
            
item = "-------------------------------\n"

def build_Menu():

            ##Numbers the Main Menu##
    global item
    global tmpcount
    count = -1
    menuS = open("Build-Main.txt", "r")
    for line in menuS:
        if line == "Quit":
            tmpcount = count
            item += ("-------------------------------\n{}. {}".format(count, line))
        elif count > 0:
            item += ("{}. {}".format(count, line))
        
        else:
            item += ("{}".format(line))
        count += 1
    menuS.close()

build_Menu()

main_menu()

placeholder = input("Congrats, you somehow broke my code")
