
from math import log



SNUM=7

def transform(snum, loop_size):
    val=1
    for i in range(loop_size):
        val*=snum
        val%=20201227
    return val


#transform(1,8)


def loop_size(snum, t):
    count=0
    val=1
    while val != t:
        val*=snum
        val%=20201227
        count+=1
    return count


door=8335663
key=8614349


#door=17807724
#key=5764801

door_loop_size = loop_size(7, door)
key_size = loop_size(7, key)
#print(transform(1, door_loop_size+key_size))
print(transform(transform(7,door_loop_size), key_size))
print(transform(transform(7,key_size), door_loop_size))



key = loop_size(1, door)

transform(transform(1,8),11)
transform(transform(1,11),8)
transform(1, 8+11)
