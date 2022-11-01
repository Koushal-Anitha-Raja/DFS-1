#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space - O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #dfs method
        #assigning the result array
        self.ans = []
        #the recursion fun will take root and 0
        self.recur(root, 0)
        #returning the result
        return self.ans
    
    #dfs function
    def recur(self, node,i):
        #if not is not present
        if not node:
            return
        
        #if the length is equal to i
        if i == len(self.ans):
            #then add the node val to each array
            self.ans.append(node.val)
            #add the right side tree first and left side tree next
        self.recur(node.right, i+1)
        self.recur(node.left, i+1)
