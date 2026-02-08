class Solution(object):
    def mostWordsFound(self, sentences):
        count2 = 0
        for i in sentences:
            count1 = len(i.split())
            if count1 > count2:
                count2 = count1
        return count2 


         
        

        