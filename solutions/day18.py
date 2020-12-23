






def parse(expr, acc, i):
    while i < len(expr):
        n = expr[i]
        if n=="(":
            n, i = parse(expr, None, i+1)
        if n==")":
            return acc, i
        if n=="*" or n=="+":
            op = n
        else:
            n=int(n)
            if acc is None:
                acc=n
            else:
                if op=="+":
                    acc+=n
                elif op=="*":
                    acc*=n
        i+=1
    return acc




def str_pop(s):
    return s[0], s[1:]

def find_chunk(expr):
    # expr must start with parenthesis
    chunk = ""
    assert expr[0] == "("
    expr = expr[1:]
    i=1
    while i != 0:
        n, expr = str_pop(expr)
        if n == "(":
            i+=1
        elif n == ")":
            i-=1
        chunk+=n
    return chunk[:-1], expr
        

def postfix_convert(prefix, postfix):
    
    op=""
    while prefix:
        current, prefix = str_pop(prefix)

        if current == "(":
            chunk, prefix = find_chunk(current+prefix)
            current = postfix_convert(chunk, "")
        
        if current=="+" or current=="*":
            op = current
        else:
            if not postfix:
                postfix=current+op
            else:
                if op=="+":
                    postfix+=current+op
                elif op=="*":
                    postfix += postfix_convert(prefix, current) + op
                    break

    return postfix





def eval_postfix(expr):
    stack = []
    for e in expr:
        if e == "+" or e == "*":
            a,b = stack.pop(), stack.pop()
            if e == "+":
                stack.append(a+b)
            else:
                stack.append(a*b)
        else:
            stack.append(int(e))
    return stack.pop()





if __name__ == "__main__":
    f = open("inputs/day18.txt", "r").read().splitlines()
    K = 0
    for s in f:
        K+=parse(s.replace(" ",""), None, 0)
    print(f"Ans 1: {K}")

    K=0
    for s in f:
        pf = postfix_convert(s.replace(" ",""), "")
        K+=eval_postfix(pf)
    print(f"Ans 2: {K}")
