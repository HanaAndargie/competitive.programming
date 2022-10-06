class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        lookup_dic={"(":")","[":"]","{":"}"}
        for i in s:
            if i in lookup_dic.keys():
                stack.append(i)==[]
            else:
                if stack==[]:
                       return 0
                else:
                    if  lookup_dic[stack[-1]]==i:
                         stack.pop()
                    else:
                         return 0
                        
                        
        if stack ==[]:
            return 1
        else:
            return 0
