import os
import time

lvlfile = os.getenv("localappdata") + "/Will_You_Snail/MyFirstLevel.lvl"

def import_level(filename):
    level = open(filename, "r")
    lvcontent = level.read().splitlines()
    level.close()
    MFLFile = open(lvlfile , "w")
    for line in lvcontent:
        MFLFile.write(line + "\n")
    MFLFile.close()

def save_level(filename):
    MFLFile = open(lvlfile, "r")
    level = open("./SavedLvls/" + filename, "w")
    for line in MFLFile.read().splitlines():
        level.write(line + "\n")
    MFLFile.close()
    level.close()

def terminal():
    print("\nWelcome to WYS Level manager Tool v1.0\nUse command 'help' to display a list of all commands\n\n")
    cmd = input("Enter Command:\n>> ")
    if cmd == "help":
        print("List of Commands:\nload : loads a level by filename\nsave : saves/exports level\nexit : quits out of this programm")
        time.sleep(1)
        terminal()
    elif cmd == "load":
        lvlname = input("Enter level filename (including filetype): ")
        if os.path.isfile("./SavedLvls/" + lvlname):
            import_level("./SavedLvls/" + lvlname)
            print("Level Loaded!")
            time.sleep(1)
            terminal()
        else:
            print("Error: Level file doesn't exist!")
            time.sleep(1)
            terminal()
    elif cmd == "save":
        lvlname = input("Please choose a Filename (including filetype): ")
        save_level(lvlname)
        print("Level Saved")
        time.sleep(1)
        terminal()

    elif cmd == "exit":
        print("Exitting...")
        time.sleep(1)
        quit()
    
    else:
        print("Error: This command doesn't exist!")
        time.sleep(1)
        terminal()

terminal()