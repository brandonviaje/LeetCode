class Solution {
public:
    int maxArea(vector<int>& height) {

        int left = 0;
        int right = height.size() - 1;
        int result = 0;

        while(left < right){
            //calculate current area
            int area = (right - left) * min(height[left],height[right]);
            result = max(result,area); //set to max area found so far

            //explore other areas based on height
            if(height[left] < height[right]){
                left++; //shift left pointer
            }else{ 
                right--; //shift right pointer
            }
        }

        return result;

        //T O(n) S O(1)
    }
};