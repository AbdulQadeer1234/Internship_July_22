class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m=max(candies)
        for i in candies:
            i=i+extraCandies
            if(i>=m):
                res.append(True)
            else:
                res.append(False)
        return res
                
        