#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : 4Sum
# LEVEL : Medium
# LINK: https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        f=[]
        if not nums:
            return f
        nums.sort()
        for i in range(0,len(nums)-1):
            t_3=target-(nums[i])
            for j in range(i+1,len(nums)-1):
                t_2=t_3-nums[j]
                c=j+1
                d=len(nums)-1
                while c<d:
                    two=nums[c]+nums[d]
                    if two<t_2:
                        c+=1
                    elif two>t_2:
                        d-=1
                    else:
                        m=[]
                        m.append(nums[i])
                        m.append(nums[j])
                        m.append(nums[c])
                        m.append(nums[d])
                        f.append(m)
                        while c<d and nums[c]==m[2]:
                            c+=1
                        while c<d and nums[d]==m[3]:
                            d-=1
                while (j+1<len(nums)-1) and (nums[j+1]==nums[j]):
                    j+=1
            while (i+1<len(nums)-1) and (nums[i+1]==nums[i]):
                i+=1
        return f

