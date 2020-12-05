


def isint(s):
    try:
        int(s)
        return True
    except:
        return False



valid_hcl = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def byr(s):
    return len(s)==4 and int(s)>=1920 and int(s)<2003

def iyr(s):
    return len(s)==4 and int(s)>=2010 and int(s)<2021

def eyr(s):
    return len(s)==4 and int(s)>=2020 and int(s)<2031

def hgt(s):
    if len(s) <= 2:
        return False

    unit = s[-2:]
    
    if not isint(s[:-2]):
        return False
    num = int(s[:-2])
    if unit=="cm":
        return num >= 150 and num <= 193
    elif unit=="in":
        return num >= 59 and num <= 76
    else:
        return False

def hcl(s):
    return s[0] == "#" and all([i in valid_hcl for i in s[1:]])


def ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid(s):
    return len(s)==9 and isint(s)
def cid(s):
    return True


isvalid = {'byr':byr, 'iyr':iyr, 'eyr':eyr, 'hgt':hgt, 'hcl':hcl, 'ecl':ecl, 'pid':pid, 'cid':cid}

if __name__ == "__main__":

    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = open("../inputs/day4.txt", "r").read().split('\n\n')
    passports = [p.split() for p in passports]
    passport_dicts = []
    for passport in passports:
        d = {}
        for l in passport:
            k,v = l.split(":")
            d[k]=v
        passport_dicts.append(d)
    
    hasfields = list(map(lambda x: all(f in x for f in fields), passport_dicts))
    print(f"ans 1: {sum(hasfields)}")

    valid = 0
    for i, passport in enumerate(passport_dicts):
        if all([isvalid[k](passport[k]) for k in passport.keys()] + [hasfields[i]]):
            valid+=1
    print(f"ans 2: {valid}")
