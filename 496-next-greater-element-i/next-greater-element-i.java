class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<>();
        Map<Integer,Integer> map = new HashMap<>();
        int [] result = new int[nums1.length];

        for(int i = 0; i < nums1.length; i ++ ){
            //put the value and index of it we can use the index as a place to store in the result
            map.put(nums1[i],i);
            result[i] = -1; //default
        }

        for(int j = 0; j < nums2.length; j++){
            //pop values from stack while current index is greater
            while(!stack.isEmpty() && nums2[j] > nums2[stack.peek()]){
                int index = stack.pop();
                //if the popped value is in the map, then set the current number that we iterate through as its greater element
                if(map.containsKey(nums2[index])){
                    result[map.get(nums2[index])] = nums2[j];
                }
            } 

            stack.push(j);
        }   
        return result;
    }
}