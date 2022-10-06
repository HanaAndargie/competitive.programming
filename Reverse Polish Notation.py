class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+ - * /":
                stack.append(int(i))
                continue
            n2=stack.pop()
            n1=stack.pop()
            result=0
            
            if i=="+":
                result=n1+n2
            elif i=="-":
                result=n1-n2
            elif i=="*":
                result=n1*n2
            else:
                result=int(float(n1/n2))
            stack.append(result)
            
        return stack.pop()
            
