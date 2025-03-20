# Write your solution here
line = input("Word: ")
spaces = 28 - len(line)
if spaces % 2 == 0:
    spaces_ba = int(spaces/2)
    mid_row = " "*spaces_ba+line+" "*spaces_ba
    if len(mid_row) < 28:
        gap = 28 - len(mid_row)
        half = int(gap / 2)
        mid_row = " "*half + mid_row + " "*half  
    print("*"*30)
    print("*" + mid_row + "*")
    print("*"*30)
elif spaces % 2 != 0:
    # spaces += 3
    space_before = int(spaces / 2)
    space_after = space_before + 1
    print("*"*30)
    print("*"+(" "*space_before)+line+(" "*space_after)+"*")
    print("*"*30)

