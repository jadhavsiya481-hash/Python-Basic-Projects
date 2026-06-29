import random, math
try:
    s = set()
    for i in range(10):
        s.add(int(input("Number:")))
    t = tuple(s)

    print("Tuple:",t)
    print("Random:",random.sample(t,3))
    print("Square Root:",math.sqrt(sum(t)))

except Exception as e:
    print("Error:",e)    