class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=[]
        if sorted(arr)==arr:
            return result
        else:
            while(arr):
                if arr[-1]!=len(arr):
                    m=arr.index(len(arr))
                    if m==0:
                        arr=arr[::-1]
                        result+=[len(arr)]
                    else:
                        arr=(arr[:m+1][::-1]+arr[m+1:])[::-1]
                        result+=[m+1,len(arr)]
                arr.pop()
        return result
        
