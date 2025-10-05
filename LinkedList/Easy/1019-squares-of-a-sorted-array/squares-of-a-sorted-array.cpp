class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> pos;
        vector<int> neg;
        vector<int> out;
        for (int i=0;i<nums.size();i++){
            if (nums[i]<0){
                neg.push_back(nums[i]);
            }
            else {
                pos.push_back(nums[i]);
            }
        }
        if (neg.size()!=0 && pos.size()==0){
            vector<int> result;
            for (int i = 0; i < neg.size(); i++) {
                result.push_back(neg[neg.size() - 1 - i]*neg[neg.size() - 1 - i]);
            }
            return result;
        }
        else if (neg.size()==0 && pos.size()!=0){
            vector<int> result;
            for (int i = 0; i < pos.size(); i++) {
                result.push_back(pos[i]*pos[i]);
            }
            return result;
        }
        else if (neg.size()==0 && pos.size()==0){
            vector<int> result;
            return result;
        }
        else if (neg.size()!=0 && pos.size()!=0){
            int i=0;
            int j=neg.size()-1;
            while (i<pos.size() || j>=0){
                if (j==-1 || ( i < pos.size() && pos[i]<-neg[j])){
                    out.push_back(pos[i]*pos[i]);
                    i+=1;
                } 
                else{
                    if (i==pos.size() || ( j >= 0 &&  pos[i]>=-neg[j]) ){
                        out.push_back(neg[j]*neg[j]);
                        j+=-1;
                    }
                }
            }
        }
        return out;
    }
};