class Solution {
    public int[] twoSum(int[] numbers, int target) {
        //scan from left side and right side
        int left = 0;
        int right = numbers.length - 1;

        //while the pointers dont cross each other
        while(left<right){
            int twoSum = numbers[left] + numbers[right];

            //if sum too big decrease right pointer i
            //if sum too small increase left pointer
            //else return left and right pointer 1 indexed
            if(twoSum == target){
                return new int[]{left + 1, right + 1};
            }else if(twoSum < target){
                left++;
            }else{
                right--;
            }
        }

        return new int[] {};
    }
}