class Solution(object):
    def judgeCircle(self, moves):
        count1 = 0 
        count2 = 0
        count3 = 0
        count4 = 0
        for i in moves:
            if i == "U":
                count1 += 1
            elif i == "D":
                count2 += 1
            elif i == "L":
                count3 += 1
            else:
                count4 += 1
        if count1 == count2 and count3 == count4:
            return True
        return False

        