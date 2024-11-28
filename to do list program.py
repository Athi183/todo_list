print("Helooo!!!! Welcome to the Todo's Tasks")
print("*************\t\tToDo List\t\t*****************")
print("======================================================================")

tasks=[]
while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as done")
    print("4. Exit")

    choice=input("Enter your choice:")
    if choice==1:
        print()
        n=int(input("How many tasks to be added:"))
        for i in range(n):
            task=input("Enter the task:")
            tasks.append({"Task":task,"Done":False})
            print("Task is added")
    elif choice==2:
       print()
       print("Tasks pending")
       for index,task in tasks:
           
       

