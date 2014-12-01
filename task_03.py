#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Executes a bubble sort function"""


def bubble_sort(nums):
    """Bubble sorts"""
    srtd = False
    while not srtd:
        sorted = True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                srtd = False
                hold = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = hold
    return nums
