while True:
    s = input()
    if s == ".":
        break
    stack = []
    for i in s:
        if i in "()[]":
            if i in "([":
                stack.append(i)
            else:
                if len(stack) == 0:
                    stack.append("d")
                    break
                if i ==")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append('d')
                    break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
        
                    
                    
                    
            
                
                
                
                