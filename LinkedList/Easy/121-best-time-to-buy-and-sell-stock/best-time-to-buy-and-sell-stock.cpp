class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i=0;
        int profit=0;
        while (i<prices.size()){
            int j=i;
            int M=0;
            while (j<prices.size() and prices[j]>=prices[i]){
                M=max((prices[j]-prices[i]),M);
                j+=1;
            }
            i=j;
            profit=max(M,profit);
            };
        return profit;




        };
        

};