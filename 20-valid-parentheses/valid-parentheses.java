class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character,Character> map = new HashMap<>(); 
        map.put('}','{');
        map.put(']','[');
        map.put(')','(');

        //Push the string onto the stack
        for(char c : s.toCharArray()){
            //Check if you get a closed bracket
            if(map.containsKey(c)){
                //if the stack is empty or the top elem in stack != the open bracket it is invalid
                if(stack.isEmpty() || stack.pop() != map.get(c)){
                    return false;
                }
            }else{
                stack.push(c);
            }   
        }
        // if the stack is empty, then that means it is valid parentheses
        return stack.isEmpty();
    }
}