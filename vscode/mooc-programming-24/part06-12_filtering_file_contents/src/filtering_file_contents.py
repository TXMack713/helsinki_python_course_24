# Write your solution here
def filter_solutions():
    correct_answers = []
    incorrect_answers = []
    with open("solutions.csv") as file:
        for line in file:
            file_contents = line.split(";")
            # operand_details = file_contents[1].split()
            answer = eval(file_contents[1])
            if answer == int(file_contents[2]):
                correct_answers.append(line)
            else:
                incorrect_answers.append(line)
    with open("correct.csv", "w") as correct_file:
        for entry in correct_answers:
            correct_file.write(entry + "\n")
    with open("incorrect.csv", "w") as incorrect_file:
        for entry in incorrect_answers:
            incorrect_file.write(entry + "\n")

if __name__ == "__main__":
    filter_solutions()
