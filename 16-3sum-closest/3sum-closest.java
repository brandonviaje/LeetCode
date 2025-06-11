class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = Integer.MAX_VALUE;

        for(int i = 0; i < nums.length -2; i++){

            // skip dupes
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while(left < right){
                int threeSum = nums[i] + nums[left] + nums[right];
                //if the difference is less than the previous one set it as the new one
                if(Math.abs(threeSum - target) < Math.abs(closest - target)){
                    closest = threeSum;
                }

                //shift pointers based on magnitude
                if(threeSum > target){
                    right--;
                }else if(threeSum < target){
                    left++;
                }else{ //return exact
                    return threeSum;
                }
            }
        }

        return closest;
    }
}