class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        dic={}
        for word in strs: 
            ws=str(sorted(word))
            if ws in dic:
                out[dic[ws]].append(word)
            else:
                dic[ws]=len(out)
                out.append([word])
        return out


        