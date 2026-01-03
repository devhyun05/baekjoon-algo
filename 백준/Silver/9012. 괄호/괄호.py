n = int(input())

for i in range(n): 
    parentheses = input()
    stack = []
    is_vps = True
    
    for p in parentheses: 
        if p == "(":
            stack.append(p)
        elif p == ")":
            if not stack:
                is_vps = False 
                break 
            else: 
                stack.pop()
                
    if not stack and is_vps:
        print("YES")
    else:
        print("NO")
    
    
        