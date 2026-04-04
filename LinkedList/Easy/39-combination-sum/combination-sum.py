class Solution(object):
    def combinationSum(self, candidates, target):
        if target<0:
            return []
        if target==0:
            return [[]]
        if len(candidates)==1:
            cand=candidates[0]
            q=target//cand
            r=target%cand
            if q>0 and r==0:
                return [[cand]*q]
            else:
                return []
        else:
            out=[]
            cand=candidates[0]
            with_cand=self.combinationSum(candidates, target-cand)
            without_cand=self.combinationSum(candidates[1:], target)
            print(without_cand)
            if len(with_cand)>0:
                out+=[[cand]+el for el in with_cand]
            if without_cand is not None:
                out+=[el for el in without_cand]
            return out





        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        