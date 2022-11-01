# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        answer=[]
        self.recur(root,0,answer)
        
        for i in answer:
            if not self.ispalindrome(i):
                return False
        return True
        
     
        
    def recur(self,root,index,answer):
        
        
        
        if len(answer)<index+1:
            answer.append([])
        if root:
            answer[index].append(root.val)
        else:
            answer[index].append(None)
        
        if root:
            self.recur(root.left,index+1,answer)
            self.recur(root.right,index+1,answer)   
   
    def ispalindrome(self,li):
        left=0
        right=len(li)-1
        while left<=right:
            if li[left]!=li[right]:
                return False
            
            left+=1
            right-=1 
        
        return True
    
        
        
        
        
        
       
    
    