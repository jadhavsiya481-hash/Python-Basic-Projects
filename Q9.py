import math

try:
    s = input("Sentence:")
    w = sorted(set(s.split()))
    
    print("Unique words:",w)
    print("Power:",math.pow(len(w),2))
    
except Exception as e:
    print("Error:",e)
