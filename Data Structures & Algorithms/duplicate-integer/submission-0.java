class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> seen = new ArrayList<>();
        for(int num : nums){
            if(seen.contains(num)){
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}