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

    public boolean DFS(TreeNode node, int targetSum, int findSum){
        //if node doesn't exist return false
        if(node == null){
            return false;
        }   

        // update current sum
        findSum += node.val;

        // check if we are at a leaf node
        if (node.left == null && node.right == null){
            return targetSum == findSum; // check if equals
        }

        // else keep exploring left or right tree
        return DFS(node.left,targetSum,findSum) || DFS(node.right,targetSum,findSum);
    }

    public boolean hasPathSum(TreeNode root, int targetSum) {
        int findSum = 0;
        return DFS(root,targetSum,findSum);
    }

    // T O(n) S O(h)
}