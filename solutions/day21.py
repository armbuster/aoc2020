



from collections import defaultdict

if __name__ == "__main__":
    f = open("../inputs/day21.txt", "r").read().split("\n")
    food = [i.split(" (contains ") for i in f]
    ingr_list = [set(i.split(" ")) for i, k in food]
    allergen_list = [tuple(i[:-1].split(", ")) for k, i in food]

    all_ingr = set.union(*ingr_list)
    all_allergen = list(set([i for k in allergen_list for i in k]))

    xref = defaultdict(set)

    food = dict(zip(allergen_list, ingr_list))
    maybe_ingr = set()

    candidate_foods = {}
    for allergen in all_allergen:
        K = set.intersection(*[food[k] for k in food.keys() if allergen in k])
        candidate_foods[allergen] = K
        maybe_ingr.update(K)
    no_allergens = all_ingr.difference(maybe_ingr)

    count=0
    for sublist in ingr_list:
        for f in sublist:
            if f in no_allergens:
                count+=1
    print(f"Ans 1: {count}")


    final_foods = []
    while candidate_foods:
        for k in candidate_foods:
            if len(candidate_foods[k])==1:
                print(len(candidate_foods))
                print(k)
                break
        final_foods.append((k, candidate_foods[k]))
        for p in candidate_foods:
            candidate_foods[p] = candidate_foods[p].difference(candidate_foods[k])
        del candidate_foods[k]
    final_foods = sorted(final_foods, key=lambda x: x[0][0])

    ans = "fqhpsl,zxncg,clzpsl,zbbnj,jkgbvlxh,dzqc,ppj,glzb"

        




