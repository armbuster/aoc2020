

def donext(i, completed, acc):
    if i in completed:
        return ("REPEAT", acc)
    if i == len(instr):
        return ("DONE", acc)


    instruction = instr[i]
    op, val = tuple(instruction.split(" "))
    val = int(val)
    if op == "nop":
        acc = donext(i+1, completed | {i}, acc)
    elif op == "acc":
        acc = donext(i+1, completed | {i}, acc + val)
    elif op == "jmp":
        acc = donext(i+val, completed | {i}, acc)
    return acc
    




if __name__ == "__main__":
    

    instr = open("../inputs/day8.txt", "r").readlines()
    acc = donext(0, set(), 0)
    print(f"Ans 1: {acc}")
            
    

    # get index of each nop
    nop_ind = [i for i, operation in enumerate(instr) if operation.split()[0] == "nop"]
    for i in nop_ind:
        instr = open("../inputs/day8.txt", "r").readlines()
        op, n = instr[i].split(" ")
        instr[i] = "jmp" + " " + n
        status, acc = donext(0, set(), 0)
        if status == "DONE":
            print("Ans 2: {acc}")


    # get index of each nop
    jmp_ind = [i for i, operation in enumerate(instr) if operation.split()[0] == "jmp"]
    for i in jmp_ind:
        instr = open("../inputs/day8.txt", "r").readlines()
        op, n = instr[i].split(" ")
        instr[i] = "nop" + " " + n
        status, acc = donext(0, set(), 0)
        if status == "DONE":
            print(f"Ans 2: {acc}")
