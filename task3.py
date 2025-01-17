stack = []
open_symbols = ['(', "[", "{"]
close_symbols = [')', "]", "}"]
string = input("Enter a string: ")
message = "Symmetric"
for symb in string:
    if symb in open_symbols:
        stack.append(symb)
    if symb in close_symbols:
        if close_symbols.index(symb) != open_symbols.index(stack.pop()):
            message = "Unsymmetric"
print(message)