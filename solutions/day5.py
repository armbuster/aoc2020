




def convert(s):
    s = s.replace("F",'0').replace("B",'1').replace("L",'0').replace("R",'1')
    return (int(s[:7], 2) , int(s[7:], 2))




if __name__ == "__main__":


    seats = map(convert, open("inputs/day5.txt", "r").readlines())
    ids = list(map(lambda x: x[0]*8+x[1], seats))
    print(f"Part 1: {max(ids)}")

    ids = sorted(ids)
    missing_seats = [a-b==2 for a,b in zip(ids[1:], ids[:-1])]
    i = missing_seats.index(True)
    print(f"Part 2: {ids[i]+1}")


