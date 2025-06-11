class Solution {
public:
    string reverseVowels(string s) {
        //set for O(1) lookups
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        //init pointers
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            //if both pointers are on a vowel swap em
            if (vowels.count(s[left]) && vowels.count(s[right])) {
                swap(s[left], s[right]);
                left++;
                right--;
            } else {
                //keep traversing the string until u come across one
                if (!vowels.count(s[left])) left++;
                if (!vowels.count(s[right])) right--;
            }
        }

        return s;

        // T O(n) S O(n)
    }
};