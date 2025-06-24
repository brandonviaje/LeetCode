class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        int left = 0;
        int right = left + 1;
        int wordCount = 0;

        //two pointers
        while(right <= sentence.length()){
            //if the right pointer at the end or is a space that means we have reached end of word or sentence
            if(right == sentence.length() || sentence.charAt(right) == ' '){
                wordCount++;
                String subStr = sentence.substring(left,right); //parse string
                if(subStr.startsWith(searchWord)){//check if it is a prefix O(m)
                    return wordCount;
                }
                //update left pointer
                left = right +1;
            }
            right++;
        }

        return -1;
    }
}