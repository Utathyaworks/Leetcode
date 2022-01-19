#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM : Search a 2D Matrix
# LEVEL : Medium
# LINK: https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        f=False
        l=0
        nr=len(matrix)
        nc=len(matrix[0])
        r=(nr*nc)-1
        while l<=r:
            mid=(l+r)//2
            k=mid//nc
            m=mid%nc
            if matrix[k][m]==target:
                f=True
                return f
            elif matrix[k][m]>target:
                r=mid-1
            else:
                l=mid+1
        return f
            
        

