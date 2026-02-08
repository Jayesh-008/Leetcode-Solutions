class Solution(object):
    def checkIfPangram(self, sentence):
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in sentence:
                return False
        return True



        
        

       
        