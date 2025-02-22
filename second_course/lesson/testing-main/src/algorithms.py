from typing import List
from collections import Counter


def find_closest_number(nums):
    closest = nums[0]
    for el in nums:
        if abs(el) < abs(closest):
            closest = el

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


def contains_duplicat(nums: List[int]) -> bool:
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


def is_anagram(s: str, t: str) -> bool:
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Input must be a string")
    if set(s) != set(t):
        return False
    for char in set(s):
        if s.count(char) != t.count(char):
            return False
    return True
