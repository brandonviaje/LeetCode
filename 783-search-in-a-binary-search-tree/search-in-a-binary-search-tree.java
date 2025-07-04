/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        
        // binary search
        while(root != null){
            if(root.val == val){
                return root;
            }else if (root.val > val){
                root = root.left; // traverse to left side
            }else{
                root = root.right; //traverse to right side
            }   
        }

        return null; 
        // T O(n) S O(1)
    }
}