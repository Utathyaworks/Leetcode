#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PROBLEM : Remove Element
# LEVEL : Easy
# LINK: https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[l]=nums[i]
                l+=1
        return l
            

