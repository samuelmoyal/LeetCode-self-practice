class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> output;
        int U = 0;
        int D = 0;
        int L = 0;
        int R = 0;
        if (matrix.size()==0){
            return output;
        }
        while ((U+D<matrix.size()) && (L+R<matrix[0].size())) {
            for (int i=L;i<matrix[0].size()-R;i++){
                output.push_back(matrix[U][i]);
            }
            U+=1;
            if (U+D==matrix.size()){
                break;
            }
            for (int j=U;j<matrix.size()-D;j++){
                output.push_back(matrix[j][matrix[0].size()-R-1]);
            }
            R+=1;
            if (L+R==matrix[0].size()){
                break;
            }
            for (int i=matrix[0].size()-R-1;i>=L;i--){
                output.push_back(matrix[matrix.size()-D-1][i]);
            }
            D+=1;
            if (U+D==matrix.size()){
                break;
            }
            for (int j=matrix.size()-D-1; j>=U;j--){
                output.push_back(matrix[j][L]);
            }
            L+=1;

        }
        return output;

        };


        
    };
