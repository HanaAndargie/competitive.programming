class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxf=max(count.values())
        lastrow=0
        for i,j in count.items():
            if j== maxf:
                lastrow+=1
        return max(len(tasks),(maxf-1)*(n+1)+lastrow)
