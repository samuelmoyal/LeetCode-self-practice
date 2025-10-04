class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        float S=0;
        for (int i=0; i<points.size()-1; i++){
            int abs_y= abs(points[i+1][1]-points[i][1]);
            int abs_x= abs(points[i+1][0]-points[i][0]);
            int m= min(abs_y,abs_x);
            int M= max(abs_y,abs_x);
            S+= m+(M-m);
        }
        return S;
        
    }
};