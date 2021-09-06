class Solution(object):
    def longestCommonPrefix(self, strs):
        min_length=0
        for u in strs:
            current_length=len(u)
            if min_length==0:
                min_length=current_length
                continue
            if(current_length < min_length):
                min_length = current_length 
        
        prex=''
        for i in range(min_length):
            flag =1
            for u in strs:
                if flag ==1:
                    prex=prex+u[i]
                    flag==2
                    continue
                if prex == u[0::i]:
                    continue
                else:
                   break 
        
        return prex


