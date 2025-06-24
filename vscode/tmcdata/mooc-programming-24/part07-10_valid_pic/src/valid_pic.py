# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    controller = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(pic)
    print(len(pic))
    if len(pic) == 11:
        date = pic[:6]
        
        identifier = pic[7:10]
        
        if date.isdigit():
            print(date) 
            if (int(date[:2]) > 31) or (int(date[2:4]) > 12):
                print(f"Day is {date[:2]}, Month is {date[2:4]}")
                return False
            else:
                if identifier.isdigit():
                    print(identifier)
                    if pic[6] == '+' or pic[6] == '-' or pic [6] == 'A':
                        number = date + identifier
                        print(f"Number: {number}")
                        remainder = int(int(number) % 31)
                        print(f"Remainder: {remainder}")
                        if pic[10] == controller[remainder]:
                            print(f"pic[10]: {pic[10]}, Controller: {controller[remainder]}")
                            return True
                        else:
                            print(f"pic[10]: {pic[10]}, Controller: {controller[remainder]}")
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        return False
        

if __name__ == "__main__":
    print(is_it_valid("080842-720N"))
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
                    
