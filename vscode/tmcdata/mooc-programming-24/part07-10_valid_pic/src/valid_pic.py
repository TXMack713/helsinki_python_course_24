# Write your solution here
#!/usr/bin/env python3
from datetime import datetime, date

def is_it_valid(pic: str):
    controller = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    print("\n")
    print(pic)
    # print(len(pic))
    if len(pic) == 11:
        given_date = pic[:6]
    
        identifier = pic[7:10]
        this_date = ''
        try:
            century = ''
            if pic[6] == '+':
                century = '18'
            elif pic[6] == '-':
                century = '19'
            elif pic[6] == 'A':
                century = '20'
            day = given_date[:2]
            month = given_date[2:4]
            yy = given_date[4:6]
            year = century + yy
            this_date = date.fromisoformat(f"{year}-{month}-{day}")
            print(f"Date given: {this_date}")
        except:
            print("Invalid date")
            print(f"Date given: {this_date}")
            return False
         
        if given_date.isdigit():
            # print(given_date) 
            if (int(given_date[:2]) > 31) or (int(given_date[2:4]) > 12):
                print(f"Day is {given_date[:2]}, Month is {given_date[2:4]}")
                return False
            else:
                if identifier.isdigit():
                    # print(f"Identifier: {identifier}")
                    if pic[6] == '+' or pic[6] == '-' or pic [6] == 'A':
                        number = given_date + identifier
                        print(f"Number: {number}")
                        remainder = int(int(number) % 31)
                        # print(f"Remainder: {remainder}")
                        letter_index = controller.find(pic[10])
                        if controller[remainder] == pic[10]:
                            # print(f"pic[10]: {pic[10]}, Controller: {letter}")
                            print(f"Remainder: {remainder}, Letter index: {letter_index}, Controller: {pic[10]}")
                            print(controller)
                            return True
                        else:
                            print(f"Remainder: {remainder}, Letter index: {letter_index}, Controller: {pic[10]}")
                            print(controller)
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
    print(is_it_valid("290103A605T"))
                    
