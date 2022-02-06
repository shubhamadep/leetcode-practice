# https://leetcode.com/problems/shortest-common-supersequence/discuss/1463754/python-3-oror-dp-solution-oror-3-parts

class Solution:
    def shortestCommonSupersequence(self, x: str, y: str) -> str:
        n=len(x)
        m=len(y)

        dp=[[-1]*(m+1)for i in range (n+1)]
        
        #1.length of longest common subsequence of x and y
        for i in range(n+1):
            for j in range(m+1):
                #base condition
                if i==0 or j==0:
                    dp[i][j]=0
                #choice 
                elif x[i-1]==y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]

                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        #2. finding the longest common subsequence string
        i=n
        j=m
        lst=[]
        while(i>0 and j>0):
            if x[i-1]==y[j-1]:
                lst.append(x[i-1])
                i-=1
                j-=1
            else:
                if (dp[i][j-1]>dp[i-1][j]):
                    j-=1
                else:
                    i-=1
        lst.reverse()
        s="".join(lst)
        
        #3. finding the supersequence-res
        res=""
        i=0
        j=0
        for c in s:
            while x[i] != c:
                res += x[i]
                i += 1
            while y[j] != c:
                res += y[j]
                j += 1
            res+=c; i+=1; j+=1
        return (res + x[i:] + y[j:])