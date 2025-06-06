class Solution {
    public int[] twoSum(int[] nums, int target) {

        //Create a hashmap
        Map<Integer, Integer> map = new HashMap<>();

        //Go through each element in arr
        for(int i = 0; i < nums.length;i++){

            int complement = target - nums[i];
            
            if(map.containsKey(complement)){
                return new int[]{map.get(complement),i};
            }

            map.put(nums[i],i);
        }
        return new int[0];
    }
}