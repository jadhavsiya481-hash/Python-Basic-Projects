try:
    s = lambda x:x*x
    l = list(map(s,range(1,21)))
    
    print("Squares:",l)
    print("Even Squares:",[i for i in l if i % 2==0])
    
except Exception as e:
    print("Error:",e)    