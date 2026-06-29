def manage_marks():
    marks=[]
    
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter mark  {i+1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a number")

    print("Average:", sum(marks)/5)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))   

    marks.sort(reverse=True)
    print("Descending Order:", marks)

manage_marks()       