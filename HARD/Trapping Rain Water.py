#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Trapping Rain Water
# LEVEL : HARD
# LINK: https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        res=0
        r=len(height)-1
        lmax=0
        rmax=0
        while l<r:
            if height[l]<=height[r]:
                if height[l]>=lmax:
                    lmax=height[l]
                else:
                    res+=(lmax-height[l])
                l+=1
            else:
                if height[r]>=rmax:
                    rmax=height[r]
                else:
                    res+=(rmax-height[r])
                r-=1
        return res

