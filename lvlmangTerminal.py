import os
import time

lvlfile = os.getenv("localappdata") + "/Will_You_Snail/MyFirstLevel.lvl"

def import_level(filename):
    try:
        level = open(filename, "r")
        lvcontent = level.read().splitlines()
        MFLFile = open(lvlfile , "w")
        for line in lvcontent:
            MFLFile.write(line + "\n")   
    except:
        print("Error: Level file not found!")
        time.sleep(0.25)
        terminal()
    finally:
        level.close()
        MFLFile.close()

def save_level(filename):
    try:
        MFLFile = open(lvlfile, "r")
        level = open("./SavedLvls/" + filename + ".lvl", "w")
        for line in MFLFile.read().splitlines():
            level.write(line + "\n")
    finally:
        MFLFile.close()
        level.close()

def list_levels():
    print("List of all Saved Levels:\n")
    for file in os.listdir("./SavedLvls"):
        if file.endswith(".lvl"):
            print(file)
    time.sleep(0.25)
    terminal()

helpstr = """
    List of Commands:

    "help" : shows this command list
    "list" : lists all saved levels
    "load" : loads a level by filename
    "save" : saves/exports level
    "exit" : quits out of this programm

"""

def terminal():
    print("\nWelcome to WYS Level manager Tool v0.1.4\nUse command 'help' to display a list of all commands\n\n")
    cmd = input("Enter Command:\n>> ")
    if cmd == "help":
        print(helpstr)
        time.sleep(0.25)
        terminal()
    elif cmd == "load":
        lvlname = input("Enter level filename: ")
        if os.path.isfile("./SavedLvls/" + lvlname + ".lvl"):
            import_level("./SavedLvls/" + lvlname + ".lvl")
            print("Level Loaded!")
            time.sleep(0.25)
            terminal()

    elif cmd == "save":
        if os.path.isdir("./SavedLvls"):
            lvlname = input("Please choose a Filename: ")
            save_level(lvlname)
            print("Level Saved")
            time.sleep(0.25)
            terminal()
        else:
            print("Error: Save Directory not Found! creating...")
            os.system("md .\SavedLvls")
            time.sleep(0.25)
            print("Directory Created, Please try Again!\n")
            terminal()
    elif cmd == "list":
        list_levels()
        time.sleep(0.25)
        terminal()

    elif cmd == "exit":
        print("Exitting...")
        time.sleep(0.25)
        quit()
    
    else:
        print("Error: This command doesn't exist!")
        time.sleep(0.25)
        terminal()

terminal()
