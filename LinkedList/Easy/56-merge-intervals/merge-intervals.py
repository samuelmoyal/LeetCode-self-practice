class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)>0:
            intervals_sorted=sorted(intervals)
            out=[]
            prep=intervals_sorted[0]
            print(intervals_sorted)
            for i in range (len(intervals_sorted)-1):
                print(prep)
                if intervals_sorted[i+1][0]<=prep[1]:
                    prep=[prep[0],max(intervals_sorted[i+1][1],prep[1])]
                else:
                    out.append(prep)
                    prep=intervals_sorted[i+1]
            out.append(prep)
            return out
        else:
            return []


        