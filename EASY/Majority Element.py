#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Majority Element
# LEVEL : Easy
# LINK: https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        el=0
        for i in range(len(nums)):
            if(c==0):
                el=nums[i]
            if el==nums[i]:
                c+=1
            else:
                c-=1
        return el
            
        

