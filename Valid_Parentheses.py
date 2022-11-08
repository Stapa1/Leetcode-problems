class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        
        """
        lenght = len(s)
        arr = []
        top = -1
        j = 0
        while(j<lenght and top<lenght):
            if top != -1:
                if arr[top]=='(' and s[j]==')' :
                    arr.pop()
                    top = top-1
                    j = j+1
                elif arr[top]=='{' and s[j]=='}':
                    arr.pop()
                    top = top-1
                    j = j+1
                elif arr[top]=='[' and s[j]==']':
                    arr.pop()
                    top = top-1
                    j =j+1
                else:
                    top = top+1
                    arr.append(s[j])
                    j = j+1
            else:
                top = top +1
                arr.append(s[j])
                j = j+1
        if (top == -1):
            return True
        else:
            return False
                
        

