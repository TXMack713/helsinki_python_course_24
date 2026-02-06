#!/usr/bin/env python 3

class Task:
    id = 1
    def __init__(self, description: str, programmer: str, workload: int, id: int = 0):
        self.id = id
        self.id = Task.id
        Task.id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.complete = False

    def is_finished(self):
        return self.complete
    
    def mark_finished(self):
        self.complete = True

    def __str__(self):
        if self.complete == False:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x 

class OrderBook:
    def __init__(self):
        self.orders = []
        self.all_programmers = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))
        self.all_programmers.append(programmer)

    def all_orders(self):
        return self.orders
    
    def mark_finished(self, id: int):
        found = ""
        for task in self.orders:
            if task.id == id:
                found = True
                task.mark_finished()
                return True
        return False
        # if found != True:
            # raise ValueError(f"Task id not found: {id}")
    
    def finished_orders(self):
        completed = []
        for task in self.orders:
            if task.is_finished() == True:
                completed.append(task)
        return completed
    
    def unfinished_orders(self):
        uncompleted = []
        for task in self.orders:
            if task.is_finished() == False:
                uncompleted.append(task)
        return uncompleted
    
    def programmers(self):
        return list(set(self.all_programmers))
    
    def status_of_programmer(self, programmer: str):
        all_programmers = self.programmers()
        complete = 0
        uncomplete = 0
        hours_complete = 0
        hours_uncomplete = 0
        for task in self.orders:
            if task.complete == True and task.programmer == programmer:
                complete += 1
                hours_complete += task.workload
            if task.complete == False and task.programmer == programmer:
                uncomplete += 1
                hours_uncomplete += task.workload
        if programmer not in self.programmers():
            raise ValueError("Programmer not found")
        
        return (complete, uncomplete, hours_complete, hours_uncomplete)

class OrderBookApplication:
    def __init__(self):
        self.__orders = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")
        programmer_workload_list = programmer_workload.split(" ")
        programmer = programmer_workload_list[0]
        workload = int(programmer_workload_list[1])
        self.__orders.add_order(description, programmer, workload)
        print("added!")
    
    def list_finished_tasks(self):
        completed_orders = self.__orders.finished_orders()
        if len(completed_orders) == 0:
            print("no finished tasks")
        else:
            for task in completed_orders:
                print(task)
    def list_unfinished_tasks(self):
        uncompleted_orders = self.__orders.unfinished_orders()
        if len(uncompleted_orders) == 0:
            print("no unfinished tasks")
        else:
            for task in uncompleted_orders:
                print(task)
    
    def mark_finished(self):
        id = input("id: ")
        marked = self.__orders.mark_finished(id)
        if marked == True:
            print("marked as finished")
        else:
            print("task not found")
            
    def list_programmers(self):
        programmers = self.__orders.programmers()
        for programmer in programmers:
            print(programmer)
    
    def get_status(self):
        programmer = input("programmer: ")
        status = self.__orders.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()        
            elif command == "2":
                self.list_finished_tasks()            
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.get_status()
            else:
                self.help()

application = OrderBookApplication()
application.execute()


