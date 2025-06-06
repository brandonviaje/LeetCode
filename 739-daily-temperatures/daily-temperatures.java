class Solution {
    public int[] dailyTemperatures(int[] temperatures) {   
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[temperatures.length];

        for(int i = 0; i < temperatures.length; i++){
            //when the stack isnt empty and while the temp[i] > other prev values
            while(!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){

                //pop the index since we found a greater element
                int index = stack.pop();

                //calculate the distance from each other
                result[index] = i - index;
            }
            
            //else push this onto stack
            stack.push(i);
        }

        return result;
        
    }
}