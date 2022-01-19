#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Trapping Rain Water
# LEVEL : Medium
# LINK: https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        f=[]
        num1=-1
        num2=-1
        c1=0
        c2=0
        for ele in nums:
            if ele==num1:
                c1+=1
            elif ele==num2:
                c2+=1
            elif c1==0:
                num1=ele
                c1=1
            elif c2==0:
                num2=ele
                c2=1
            else:
                c1-=1
                c2-=1
        cn1=0
        cn2=0
        if num1==num2:
            f.append(num1)
            return f
        for ele in nums:
            if ele==num1:
                cn1+=1
            if ele==num2:
                cn2+=1
        if cn1>(len(nums)//3):
            f.append(num1)
        if cn2>(len(nums)//3):
            f.append(num2)
        return f

