# Balanced Parentheses:
# Given a string with alphanumeric characters, numbers, and random open and closed parentheses
# return a string where the parentheses are correct
# for every opening parenthesis there should be 1 closing parentheses

# print(balancedParentheses("((())))))")) # "((()))"
# print(balancedParentheses("a)bcd(efg)12)((asf)))"))  # "abcd(efg)12((asf))"
# print(balancedParentheses("a(b()cklm(()))d)e"))  # "a(b()cklm(()))de"



def balancedParentheses(strs):
    arr = []
    open_p = 0
    
    for char in strs:
        #  Add character 
        if char != '(' and char != ')':
            arr.append(char)
            continue
        
        # Add starting parenteses
        if char == '(':
            open_p += 1
            arr.append(char)
            continue
        
        # Check edge case:
        # skiping first close and exess of close
        if open_p <= 0 and char == ')':
            continue
        
        # Remove closing  
        else:
            open_p -= 1
            arr.append(char)

    return ''.join(arr)


print(balancedParentheses("((())))))")) # "((()))"
print(balancedParentheses("a)bcd(efg)12)((asf)))"))  # "abcd(efg)12((asf))"
print(balancedParentheses("a(b()cklm(()))d)e"))  # "a(b()cklm(()))de"

