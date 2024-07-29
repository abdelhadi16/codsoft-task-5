tasks = []

def addtask():
    task = input("enter task : ")
    tasks.append(task)
    print(f"task '{task}' add .")
def listtasks() :
    if not tasks :
        print("thre is no tasks currently")
    else :
      print("corrent tasks :")
      for index, task in enumerate(tasks) :
          print(f"task #{index}. {task}")  
def delettask():
    listtasks()
    try:
        tasktodelet = int(input("choise the # to task :"))
        if tasktodelet >= 0 and tasktodelet < len(tasks) :
           tasks.pop(tasktodelet)
           print(f" task #{tasktodelet} deleted")
        else :
            print(f" task #{tasktodelet} was not found")
    except:
        print("invalid input")



if __name__ == "__main__": 
    #create a loop to run the app
    print("welcome to the to do list app :")
    while True :
        print("\n")
        print("please select one of the following options")
        print("------------------------------------------")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.List tasks")
        print("Quit")
        choise = input("enter your choise :")
        if (choise == "1") :
            addtask()
        elif (choise == "2") :
            delettask()
        elif (choise == "3") :
            listtasks()
        elif (choise == "4") :
            break
        else:
            print("invalid input please try again.")