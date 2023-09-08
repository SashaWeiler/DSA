from ArrayStack import ArrayStack

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    
    S = ArrayStack()
    
    for c in expr:
        if c in lefty: # If it's a lefty you want to put it right away
            S.push(c)
        # if it's a righty you want to first check that there is something in the stack
        # If there is not, you know a right symbol was encountered without an opening left symbol
        elif c in righty: 
            if S.is_empty():
                return False
            # Next you need to check that if there is a left symbol already in the stack, that
            # it is the counterpart to the symbol taken from the stack, ie the stack should have ( if the character
            # in the expression is ) they both would be at index 0 of lefty and righty respectively
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

expression = '({[]})'
print(is_matched(expression))

expression2 = '(()'
print(is_matched(expression2))

expression3 = '[(y+2)-(5+x)]'
print(is_matched(expression3))