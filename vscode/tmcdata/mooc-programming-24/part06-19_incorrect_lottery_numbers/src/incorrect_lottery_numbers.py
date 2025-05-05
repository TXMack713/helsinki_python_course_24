# Write your solution here
def filter_incorrect():
    correct_numbers = []
    with open("lottery_numbers.csv") as my_file:
        for line in my_file:
            line = line.rstrip("\n")
            print("Checking line", line)
            this_week = line.split(" ")
            week_info = this_week[1].split(";")
            week_number = week_info[0]
            numbers = week_info[1].split(",")
            valid_nums = []
            if week_number.isdigit():
                if len(numbers) == 7:
                    print("Week number", week_number)
                    print("Numbers", numbers)
                    for num in numbers:
                        num.strip()
                        if not num.isdigit():
                            pass
                        else:
                            if int(num) < 1 or int(num) > 39:
                                pass
                            else:
                                print(num)
                                if valid_nums.count(int(num)) == 0:
                                    valid_nums.append(int(num))
                                # else:
                                #     pass
                else:
                    pass
                if len(valid_nums) < 7 or len(valid_nums) > 7:
                    pass
                else:
                    correct_numbers.append(line)
                    print("Good line", line)
            else:
                pass

    with open("correct_numbers.csv", "w") as file:
        for entry in correct_numbers:
            file.write(entry + "\n")
    
if __name__ == "__main__":
    filter_incorrect()
    
