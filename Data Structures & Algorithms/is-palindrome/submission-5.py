class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        j=len(s)-1
        
        s=s.lower()
        for c in s:
            while not s[j].isalnum() and j>0:
                j-=1
            if not c.isalnum():
                continue
            print("firsr char is")
            print(c)
            print("second char is")
            print(s[j])
            if c != s[j]:
                return False
            j-=1
                

            
        return True