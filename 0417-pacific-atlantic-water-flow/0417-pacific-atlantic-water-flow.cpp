class Solution {
private:
    void dfs(int x, int y, vector<vector<int>>& heights, vector<vector<bool>>& visited, int rows, int cols) {
        visited[x][y] = true;
        vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        
        for (auto dir : directions) {
            int newX = x + dir[0];
            int newY = y + dir[1];

            if (isValid(newX, newY, rows, cols) && !visited[newX][newY] &&
                heights[newX][newY] >= heights[x][y]) {
                dfs(newX, newY, heights, visited, rows, cols);
            }
        }
    }

    bool isValid(int x, int y, int rows, int cols) {
        return x >= 0 && y >= 0 && x < rows && y < cols;
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int rows = heights.size();
        int cols = heights[0].size();

        vector<vector<bool>> pacificVisited(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlanticVisited(rows, vector<bool>(cols, false));

        // Pacific: top row & left column
        for (int i = 0; i < rows; i++) dfs(i, 0, heights, pacificVisited, rows, cols);
        for (int j = 0; j < cols; j++) dfs(0, j, heights, pacificVisited, rows, cols);

        // Atlantic: bottom row & right column
        for (int i = 0; i < rows; i++) dfs(i, cols - 1, heights, atlanticVisited, rows, cols);
        for (int j = 0; j < cols; j++) dfs(rows - 1, j, heights, atlanticVisited, rows, cols);

        // Collect result
        vector<vector<int>> result;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pacificVisited[i][j] && atlanticVisited[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        return result;
    }
};
