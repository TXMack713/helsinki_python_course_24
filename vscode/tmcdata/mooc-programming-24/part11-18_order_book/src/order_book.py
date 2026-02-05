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
        if found != True:
            raise ValueError(f"Task id not found: {id}")
    
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

if __name__ == "__main__":
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(4)
    orders.mark_finished(5)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)
    
    status = orders.status_of_programmer("Adele")
    print(status)
