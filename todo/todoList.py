tasks = [] 

def add_task(task):
    tasks.append(task)
    print(f"task '{task}' added!") 

def view_tasks():
    if not tasks :
        print("No tasks found, please enter one!")        
    for i, task in enumerate(tasks, 1):
        print( f"{i}.  {task}")

def delete_tasks(task_num):
    if 0 < task_num<= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"task '{removed}' deleted!")
    else:
        print("Invalid task number!")

while True:
    print(f"\n1. enter a task  2. View tasks  3. Delete a Task  4. Exit")
    choice = input("enter your choice : ")  

    if choice == "1":
        task = input("Enter task : ")   
        add_task(task)

    elif choice == "2":
        print("your tasks : ")
        view_tasks()
    
    elif choice == "3":
        task_num = int(input("enter the task number to delete :  "))
        delete_tasks(task_num)

    elif choice == "4":
        break 

    else :
        print("invalid choice, Try again!")    

    

   

