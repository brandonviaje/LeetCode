class Solution {
public:
    int lengthOfLastWord(string s) {

        int length = 0;
        int i = s.length() - 1;

        // skip extra white spaces
        while (i >= 0 && s[i] == ' ') {
            i--;
        }

        // count the length of the last word
        while (i >= 0 && s[i] != ' ') {
            length++;
            i--;
        }

        return length;
    }
};