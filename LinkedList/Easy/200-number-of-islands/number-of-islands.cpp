class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        if (grid.size()==0){
            return count;
        }
        bitset <90000> seen;
        vector<pair <int,int>> to_visit;
        int i=0;
        int j=0; 
        for (int i=0; i<grid.size();i++){
            for (int j=0; j<grid[0].size(); j++){
                if (grid[i][j]=='1' && seen[(i)*grid[0].size()+j]==0){
                    pair <int,int> start= {i,j};
                    to_visit.push_back(start);
                    while (to_visit.size()>0){
                        pair<int,int> p = to_visit.back();
                        to_visit.pop_back();
                        int i = p.first;
                        int j = p.second;
                        seen[(i)*grid[0].size()+j]=1;
                        if (i+1<grid.size() && grid[i+1][j]=='1' && seen[(i+1)*grid[0].size()+j]==0){
                            to_visit.push_back(pair <int,int> {i+1,j});
                        }
                        if (i-1>=0 && grid[i-1][j]=='1' && seen[(i-1)*grid[0].size()+j]==0){
                            to_visit.push_back(pair <int,int> {i-1,j});
                        }
                        if (j+1<grid[0].size() && grid[i][j+1]=='1' && seen[(i)*grid[0].size()+j+1]==0){
                            to_visit.push_back(pair <int,int> {i,j+1});
                        }
                        if (j-1>=0 && grid[i][j-1]=='1' && seen[(i)*grid[0].size()+j-1]==0){
                            to_visit.push_back(pair <int,int> {i,j-1});
                        }
                    for (auto [x, y] : to_visit) {
                        std::cout << "(" << x << "," << y << ") ";
                    }
                    std::cout << "\n";
                    };
                    count+=1; 
                };
            };
        };
        return count;
    };
};