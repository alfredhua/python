class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        min_length=0
        for u in strs:
            current_length=len(u)
            if min_length==0:
                min_length=current_length
                continue
            if(current_length < min_length):
                min_length = current_length 
        
        prex=strs[0]
        for i in range(1,min_length):
            prex=self.get_prex(prex,u[i])
            if not prex:
                break
        return prex
           
    def get_prex(self,prex,u):
        index = 0
        length=min(len(prex),len(u))
        while index<length and prex[index] ==u[index]:
            index+=1
        return prex[:index]


print(Solution().longestCommonPrefix(["flower","flow","flight"]))

        


