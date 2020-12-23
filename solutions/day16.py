




def range_from_str(s):
    lower, upper = tuple([int(i) for i in s.split("-")])
    return range(lower, upper+1)



def parse_rules(rules):
    rules = [r.split(": ")[1] for r in rules]
    ranges = [tuple(r.split(" or ")) for r in rules]
    rules = [(range_from_str(first), range_from_str(second)) for first, second in ranges]
    return rules


def is_valid_ticket(ticket, rule_list):
    return all(map(lambda x: any([x in r for r in rule_list]), ticket))


def which_rule(entries, rule_list):
    for ix, (first, second) in enumerate(rule_list):
        if is_valid_ticket(entries, [first, second]):
            return ix
    return -1


def how_many_rules(entries, rule_list):
    k=0
    for ix, (first, second) in enumerate(rule_list):
        if is_valid_ticket(entries, [first, second]):
            k+=1
    return k


if __name__ == "__main__":
    f = open("../inputs/day16.txt", "r").read()
    chunks = f.split("\n\n")
    rules = chunks[0].splitlines()
    tickets = chunks[2].splitlines()
    tickets = [[int(i) for i in l.split(",")] for l in tickets[1:]]
    rules = parse_rules(rules)
    
    rules_flat = [r for ruleset in rules for r in ruleset]

    valid_tickets = []
    error_rate = 0
    for ticket in tickets:
        for i in ticket:
            valid = False
            for r in rules_flat:
                if i in r:
                    valid = True
                    break
            if not valid:
                error_rate += i
    print(f"Ans 1: {error_rate}")


    myticket = [int(i) for i in chunks[1].split("\n")[1].split(",")]

    valid_tickets = list(map(lambda x: is_valid_ticket(x, rules_flat), tickets))
    tickets = [t for ix, t in enumerate(tickets) if valid_tickets[ix]]
    tickets.append(myticket)

    tickets_df = pd.DataFrame(tickets)
    rulecounts = tickets_df.apply(lambda x: how_many_rules(x, rules), 0)
    tickets_df = tickets_df.iloc[:,np.argsort(rulecounts)]
    #rulecounts = tickets_df.apply(lambda x: how_many_rules(x, rules), 0)
    #rule_indices = tickets_df.apply(lambda x: which_rule(x, rules), 0)

    field_rules = []
    for i in range(tickets_df.shape[1]):
        rule_ind = which_rule(tickets_df.iloc[:, i], rules)
        field_rules.append(rule_ind)
        rules[rule_ind] = (range(0,0), range(0,0))

    arr = np.where([f in range(0,6) for f in field_rules])[0]
    myticket = np.array(myticket)[np.argsort(rulecounts)]
    ans2 = np.prod(myticket[arr])
    print(f"Ans 2: {ans2}")
    








            










