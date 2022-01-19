#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Pascal's Triangle
# LEVEL : Easy
# LINK: https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        
        if numRows == 1:
            res.append([1])
        elif numRows == 2:
            res.append([1])
            res.append([1,1])
        else:
            res.append([1])
            for i in range(1, numRows):
                curr = []
                curr.append(1)
                for j in range(0, len(res[i-1]) - 1):
                    curr.append(res[i-1][j] + res[i-1][j+1])
                curr.append(1)
                res.append(curr)
        return res

