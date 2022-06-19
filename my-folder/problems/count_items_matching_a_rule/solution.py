class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        for i in items:
            if ruleKey=="type"and ruleValue==i[0]:
                count+=1
            elif ruleKey=="color"and ruleValue==i[1]:
                count+=1
            elif ruleKey=="name"and ruleValue==i[2]:
                count+=1
        return count
        