class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> list = new ArrayList<>();
        List<List<Integer>> finalList = new ArrayList<>();
        solve(finalList,list,0,nums,nums.length);
        return finalList;
    }
    public static void solve(List<List<Integer>> finalList, List<Integer> list, int cur, int[] nums, int l){
        if(cur==l){
            List<Integer> subSet=new ArrayList<>(list);
            finalList.add(subSet);
            return;
        }
        
        solve(finalList,list,cur+1,nums,l);
        list.add(nums[cur]);
        solve(finalList,list,cur+1,nums,l);
        list.remove(list.size() - 1);
        
    }
}