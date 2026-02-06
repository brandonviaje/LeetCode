class Solution 
{
public:
    int trap(vector<int>& height) 
    {
        /*
        *   to get how much water it can fill at a certain index, you subtract the min of leftMax and rightMax with the current height.
        *   min of leftMax and rightMax determines the bound since water can only fill <= min(leftMax,rightMax)
        *
        *   smaller boundary is the limiting factor because water would
        *   spill over that side first.
        */
        int l {}, r {static_cast<int>(height.size()-1)};
        int leftMax {height[l]}, rightMax {height[r]};
        int result {};

        while(l<r)
        { 
            // if left max is the smaller bound, shift to right and update result
            if(leftMax < rightMax)
            {
                l++;
                leftMax = max(leftMax, height[l]);   // update leftMax 
                result += leftMax - height[l];
            }
            else  // if right max is the smaller bound, shift to left and update result
            {
                r--;
                rightMax = max(rightMax, height[r]); // update rightMax 
                result += rightMax - height[r];
            }
        }

        return result;
    }
};