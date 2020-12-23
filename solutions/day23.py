


if __name__ == '__main__':
    #cups = "496138527"
    #cups = "389125467"
    cups = "123456789"
    cups = [int(i) for i in cups]
    n = len(cups)
    tot = sum(cups)

    current = 0
    for i in range(10):
        print(cups, current)
        if i%100==0:
            print(i)
        a,b,c = tuple([(current+i)%n for i in range(1,4)])
        a_val, b_val, c_val = cups[a], cups[b], cups[c]
        
        dest = cups[current]-1
        current_val = cups[current]
        
        while dest in {a_val, b_val, c_val,0}:
            dest-=1
            if dest<=0:
                dest = max(cups)

        
        # get index of dest
        # for dest_ix, i in enumerate(cups):
        #     if i==dest:
        #         break
        
        
        for ind in sorted([a,b,c], reverse=True):
            del cups[ind]

        
        # get index of dest again
        for ix, i in enumerate(cups):
            if i==dest:
                break
        
        for k in [c_val,b_val,a_val]:
            cups.insert(ix+1, k)
        
        while cups[current] != current_val:
            cups = [cups[-1]] + cups[:-1]

        current = (current+1) % n
        
        
        assert len(cups) == n
        assert sum(cups) == tot
    for ix, i in enumerate(cups):
        if i==1:
            break
    
    s = ""
    ix = (ix+1)%n
    while cups[ix]!=1:
        s+=str(cups[ix])
        ix = (ix+1)%n
    print(f"Ans 1: {s}")







