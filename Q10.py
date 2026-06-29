import math, random
h = {}
while True:
    print("\n1.Basic 2.Scintific 3.Random 4.Save 5.History 6.Exit")
    ch = input("Choice:")

    if ch == "1":
        try:
            a = float(input("A: "))
            b = float(input("B: "))
            r = a + b
            print(r)
        except:
            print("Invalid")

    elif ch == "2":
        try:
            n = float(input("Number:"))
            r = math.sqrt()
            print(r)
        except:
            print("Invalid")

    elif ch == "3":
        r = random.randint(1,100)
        print(r)

    elif ch == "4":
        try:
            h[input("Time: ")] = r
        except:
            print("Calculate something before saving.")

    elif ch == "5":
        print(h)     

    elif ch == "6":
        break 