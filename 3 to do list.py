tasks =["study python","cpp","java","javascript"]
while True:
    print("1.Add task")
    print("2.view task")
    print("3.delete task")
    print("4.exit")
    choice =int(input("Enter your choice:"))
    if choice ==1:
        task =input("enter the task you want to add:")
        tasks.append(task)
        print("task added successfully:")
    elif choice == 2:
        print("Your tasks are:")

        if len(tasks) == 0:
            print("No tasks available")
        else:
            for task in tasks:
                print("-", task)

    elif choice ==3:
       task = input("enter the task that you want to remove:") 
       if task in tasks:
            tasks.remove(task)
            print("task removed successfully:")
       else:
            print("task not found.")
    elif choice ==4:
        print("exit the program.")
        break
    else:
      print("invalid choice")