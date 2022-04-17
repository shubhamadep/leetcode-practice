class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for stone in asteroids:
    
            stoneKilled = False
            while stack and stack[-1] > 0 and stone < 0:
                
                if stack and abs(stack[-1]) == abs(stone):
                    stack.pop()
                    stoneKilled = True
                    break
                    
                if abs(stack[-1]) > abs(stone):
                    stoneKilled = True
                    break
                    
                stack.pop()
            
            if not stoneKilled:
                stack.append(stone)
        
        return stack
                
                
                
                
                    