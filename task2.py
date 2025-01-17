from collections import deque
def check_string(string):
    string = string.strip()
    d = deque()
    for symb in string:        
        if symb != " ":
            d.append(symb.lower())    
    for _ in range (int(len(d)/2)):        
        if d.popleft() != d.pop():
            print("String is not a palindrome")
            return
    print("String is a palindrome")    


check_string("xcv vcx")