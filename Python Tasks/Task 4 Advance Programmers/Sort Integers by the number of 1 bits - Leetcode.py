class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        arr.sort()
        l1=[]
        ans=[]
        for i in arr:
            l1.append([i, bin(i).count("1")])  #[[0,0],[1,1],[2,1],[3,2],[4,1],[5,2],[6,2],[7,3],[8,1]]
            l1.sort(key = lambda x: x[1])      #[[0,0],[1,1],[2,1],[4,1],[8,1],[3,2],[5,2],[6,2],[7,3]]

        for element, bit_count in l1:
            ans.append(element)

        return ans
    
        
       
        