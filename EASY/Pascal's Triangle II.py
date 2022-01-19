#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Pascal's Triangle II
# LEVEL : Easy
# LINK: https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        
        if rowIndex == 0:
            return [1]
            res.append([1])
        elif rowIndex == 1:
            res.append([1])
            res.append([1,1])
            return [1,1]
        else:
            res.append([1])
            for i in range(1, rowIndex+1):
                curr = []
                curr.append(1)
                for j in range(0, len(res[i-1]) - 1):
                    curr.append(res[i-1][j] + res[i-1][j+1])
                curr.append(1)
                res.append(curr)
        return curr

