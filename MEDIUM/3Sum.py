#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : 3Sum
# LEVEL : Medium
# LINK: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        f=[]
        for i in range(0,len(nums)-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                b=i+1
                c=len(nums)-1                
                while b<c:
                    if nums[b]+nums[c]==(-nums[i]):
                        f.append([nums[i],nums[b],nums[c]])
                        while b<c and nums[b]==nums[b+1]:
                            b+=1
                        while b<c and nums[c]==nums[c-1]:
                            c-=1                    
                        b+=1
                        c-=1
                    elif nums[b]+nums[c]>(-nums[i]):
                        c-=1
                    else:
                        b+=1
        return f

