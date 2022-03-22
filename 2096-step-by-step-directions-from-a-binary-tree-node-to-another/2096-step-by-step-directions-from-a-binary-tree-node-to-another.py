class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return ""
        
        result=""
        
        self.startpath=""
        self.destpath=""
        
        self.dfs(root,startValue,True)
        self.dfs(root,destValue,False)
        
        self.startpath=self.startpath[::-1]
        self.destpath=self.destpath[::-1]
        
        i=0
        j=0
        
        while i<len(self.startpath) and j<len(self.destpath):
            if self.startpath[i]==self.destpath[j]:
                i+=1
                j+=1
            else:
                break
                
        while i<len(self.startpath):
            result+="U"
            i+=1
            
        result+=self.destpath[j:]
        
        return result
    
    def dfs(self,root,startValue,start):
        
        if not root:
            return False
        
        if root.val==startValue:
            return True
        
        left=self.dfs(root.left,startValue,start)
        
        if left:
            if start:
                self.startpath+="L"
            else:
                self.destpath+="L"
            return True
        
        right=self.dfs(root.right,startValue,start)
        
        if right:
            if start:
                self.startpath+="R"
            else:
                self.destpath+="R"
            return True
        
        return False