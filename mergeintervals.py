class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge_interval=[]
        intervals=sorted(  intervals)
        
        if len(intervals)==0:
            return merge_interval
        temp_interval=intervals[0]
        for current_interval in intervals[1:]:
            if current_interval[0]<=  temp_interval[1]:
                temp_interval[1]=max( temp_interval[1],current_interval[1])
            else:
                merge_interval.append( temp_interval)
                temp_interval= current_interval
        merge_interval.append( temp_interval)
        return merge_interval
                
