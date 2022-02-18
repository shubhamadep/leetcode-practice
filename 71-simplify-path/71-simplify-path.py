class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        
        stack = []
        for portion in path.split('/'):
            if portion == '..':
                if stack:
                    stack.pop()
            elif not portion or portion == '.':
                continue
            else:
                stack.append(portion)
        
        
        result = "/" + "/".join(stack)
        return result
            