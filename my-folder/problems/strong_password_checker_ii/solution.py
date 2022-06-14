class Solution:
    def strongPasswordCheckerII(self,password):
        l="abcdefghijklmnopqrstuvwxyz"
        u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d="0123456789"
        s="!@#$%^&*()-+"
        count=0
        for i in l:
            if i in password:
                count+=1
                break
        for i in u:
            if i in password:
                count+=1
                break
        for i in d:
            if i in password:
                count+=1
                break
        for i in s:
            if i in password:
                count+=1
                break
        if count!=4:
            return(False)
        for i in l:
            if i*2 in password:
                count+=1
                break
        for i in u:
            if i*2 in password:
                count+=1
                break
        for i in d:
            if i*2 in password:
                count+=1
                break
        for i in s:
            if i*2 in password:
                count+=1
                break
        if count!=4:
            return(False)
        return len(password)>7
        
        
            
        