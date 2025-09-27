class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        tot=nums1+nums2
        tot.sort()
        print(tot)
        if len(tot)==0:
            return 0
        else:
            if len(tot)%2==1:
                return tot[(len(tot)-1)/2]
            if len(tot)%2==0:
                print (tot[(len(tot)-1)/2])
                print(tot[(len(tot)-1)/2+1])
                s=tot[(len(tot)-1)/2] + tot[( len(tot) -1 ) / 2  + 1 ]

                out= float(s)/2
                print(out)
                return out



        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        