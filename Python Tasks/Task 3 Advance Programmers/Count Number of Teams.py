class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        # Brute force Approach but not an optimal solution
        
        # for i in range(len(rating)):
            # for j in range(i+1,len(rating)):
                # for k in range(j+1,len(rating)):
                    # if(rating[i]<rating[j]<rating[k] or rating[i]>rating[j]>rating[k]):
                        # count+=1
        # return count
        
        # O(n^2) time complexity 
        
        #For each i, find how many rating[j] where j > i are greater 
	    #or smaller  than rating[i]. Store the numbers in g[i] and s[i], respectively.
        n = len(rating)
        g, s = [0] * n, [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    g[i] += 1
                else:
                    s[i] += 1
                    
        #For every rating[i] and rating[j] where i < j, 
		#find how many rating[k] where k > j can form 
		#a valid team with rating[i] and rating[j]. 
		#The number of rating[k] is simply g[j] 
		#if rating[i] < rating[j] or s[j] if rating[i] > rating[j].
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    ans += g[j]
                else:
                    ans += s[j]
        return ans
        
        
        