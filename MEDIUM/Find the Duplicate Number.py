#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Find the Duplicate Number
# LEVEL : Medium
# LINK: https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=[0]*len(nums)
        for i in range(len(nums)):
            if k[nums[i]]==1:
                return nums[i]
            else:
                k[nums[i]]+=1

