class ToDolist():
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task):
        self.tasks.append({"task":task,"done":False})
        print(f"Task {task} added sucessfully")
    
    def remove_task(self,task):
        for t in self.tasks:
            if t["task"]==(task):
                self.tasks.remove(t)
                print("Task removed from your ToDo list")
            else :
                print("Task  is not found") 
            

    def dislpay_task(self):
        if self.tasks:
            print("Your ToDo_List : ")
            for i,task in enumerate(self.tasks,start=1) :
                status="Done" if task["done"] else "NotDone"
                print(f"{i}.{task["task"]} - {status}")
          
        else:
            print("Your ToDo_list is empty")
    
    def mark_completed(self,task):
        task_i=int(input("Enter the Task  number to mark as done : "))-1
        if 0 <= task_i <len(self.tasks):
            self.tasks[task_i]["done"]=True
            print("Task marked as completed !")
        else:
            print("invalid task number")
       

def main():
    todolist=ToDolist()

    while True:

        print("Choose the option from the below")
        print("1.AddTask")
        print("2.RemoveTask")
        print("3.DisplayTask")
        print("4.MarkTask as completed")
        print("5.Exit from your ToDo_list")

        choice = input("Enter you choice :")
        
        if choice == "1":
            task = input("Enter the Task to add in your ToDo_list:")
            todolist.add_task(task)

        elif choice == "2":
            task = input("Enter the Task  to remove from your ToDo_list:")
            todolist.remove_task(task)
        
        elif choice == "3":
            todolist.dislpay_task()
           

        elif choice == "4":
            todolist.mark_completed(task)
            

        elif choice == "5":
            print("Exit from ToDo_list..!") 
            break  

        else :
            print("invalid choice!")
main()       
       



    

       

    
