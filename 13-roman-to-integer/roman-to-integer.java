class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        for (int i = 0; i < s.length(); i++) {
            int curr = map.get(s.charAt(i));
            int next = 0;

            // Safe to check i+1 only if within bounds
            if (i + 1 < s.length()) {
                next = map.get(s.charAt(i + 1));
                if (curr < next) {
                    sum += (next - curr);
                    i++; // Skip the next char because it's part of the pair
                    continue;
                }
            }

            sum += curr;
        }

        return sum;
    }
}