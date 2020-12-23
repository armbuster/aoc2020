
from collections import defaultdict
import re
import numpy as np

def generate_regex(clause):
    next_clause = ruleset[clause]
    if next_clause in ['a','b']:
        return next_clause
    results = []
    for subclause in next_clause:
        expr=''
        for rule in subclause:
            expr+=generate_regex(int(rule))
        expr = "("+expr+")"
        results.append(expr)
    return "(" + "|".join(results) + ")"



def parse_rules(rules):

    ruleset = defaultdict(list)
    for r in rules:
        a,b = tuple(r.split(": "))
        c=None
        a = int(a)
        if b in ['"a"', '"b"']:
            ruleset[a]=b.replace('"','')
        else:
            if "|" in b:
                b,c = tuple(b.split(" | "))
            ruleset[a].append(tuple([int(k) for k in b.split(" ")]))
            if c is not None:
                ruleset[a].append(tuple([int(k) for k in c.split(" ")]))
    return ruleset


def print_state(expr, i, level):
    return str(i) +"  "+ expr + "  " + str(level)



def parse_expr(expr, i, level):
    
    print(print_state(expr, i, level))
    if expr == "":
        return expr
    if ruleset[i] in ['a', 'b']:
        if ruleset[i] == expr[0]:
            return expr[1:]
        else:
            return expr
    
    parsed_strings = [expr]
    for clause in ruleset[i]:
        expr__ = expr
        match = True
        for rule in clause:
            reduced_expr = parse_expr(expr__, rule, level+1)
            if len(reduced_expr) == len(expr__):
                match = False
                break
            else:
                #print(i)
                expr__ = reduced_expr
        if match:
            parsed_strings.append(expr__)
            #break
    
    k = np.argmin([len(i) for i in parsed_strings])
    return parsed_strings[k]
    
 
        








if __name__ == "__main__":
    f = open("../inputs/day19_test.txt", "r").read()
    rules, patterns = f.split("\n\n")
    rules = rules.splitlines()
    patterns = patterns.splitlines()
    ruleset = parse_rules(rules)
    
    regex = "^"+generate_regex(0)+"$"
    regex = re.compile(regex)

    i=0
    for p in patterns:
        if regex.match(p):
            print(p)
            i+=1
    print(f"Ans 1: {i}")
    


    ########################
    ####   part 2 ##########
    ########################


    f = open("../inputs/day19.txt", "r").read()
    rules, patterns = f.split("\n\n")
    rules = rules.splitlines()
    patterns = patterns.splitlines()
    ruleset = parse_rules(rules)

    # count how many 42s there are on the start
    # count how many 38s there are on the end
    # if the number of 42s is greater than the number of 38s, match

    fortytwo = re.compile(generate_regex(42))
    thirtyone = re.compile(generate_regex(31))

    count=0
    for f in patterns:
        a = 0
        b = 0
        while f and fortytwo.match(f):
            i,j = fortytwo.match(f).span()
            f = f[j:]
            a+=1
        while f and thirtyone.match(f):
            i,j = thirtyone.match(f).span()
            f = f[j:]
            b+=1
        if a>b and b>0 and f == "":
            count+=1
    print(f"Ans 2: {count}")