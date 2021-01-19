class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        System.out.println(m);
        int visi[][] = new int[m][n];
        return findallpath(obstacleGrid,0,0,m,n,visi);
    }
    
    public static int findallpath(int[][] obstacleGrid,int r,int c,int m, int n,int[][] visi){
        if(r==m || c==n || obstacleGrid[r][c]==1){
            return 0;
        }
        else if(r==m-1 && c==n-1){
            return 1;
        }
        else if(visi[r][c]!=0){
            return visi[r][c];
        }
        else{
            visi[r][c] = findallpath(obstacleGrid,r+1,c,m,n,visi) + findallpath(obstacleGrid,r,c+1,m,n,visi);
            return visi[r][c];
        }
        
    }
}