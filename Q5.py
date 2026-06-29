def student_database():
    db = {}
    while True:
        print("\n1.Add 2.Search 3.Display 4.Exit")
        try:
            ch = input("Choice:")
            if ch == '1':
                r = int(input("Roll:"))
            elif ch == '2':
                r = int(input("Roll to search:"))
                s = db.get(r)
                print(s if s else "Not Found")
            elif ch == '3':
                for k,v in db.items(): print(f"Roll {k}: {v}")
            elif ch == '4':
                break
        except ValueError:
            print("Invalid input")

student_database()                            