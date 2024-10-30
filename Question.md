# 1671. Minimum Number of Removals to Make Mountain Array

__Type:__ Hard <br>
__Topics:__ Array, Binary Search, Dynamic Programming, Greedy <br>
__Companies:__ Paypal, Google, Microsoft, Amazon <br>
__Leetcode Link:__ [Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array) <br>
__Reference Video:__ [Minimum Number of Removals to Make Mountain Array - Leetcode 1671 - Python](https://youtu.be/Ys-q9qPpleY)
<hr>

You may recall that an array `arr` is a __mountain array__ if and only if:

- `arr.length >= 3`
- There exists some index `i` (__0-indexed__) with `0 < i < arr.length - 1` such that:
    - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
    - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `nums​​​`, return _the __minimum__ number of elements to remove to make_ `nums​​​` _a **mountain array**_.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ nums = [1,3,1] <br>
__Output:__ 0 <br>
__Explanation:__ The array itself is a mountain array so we do not need to remove any elements.

- __Example 2:__ <br>
__Input:__ nums = [2,1,1,5,6,2,3,1] <br>
__Output:__ 3 <br>
__Explanation:__ One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
<hr>

### Constraints:
- `3 <= nums.length <= 1000`
- <code>1 <= nums[i] <= 10<sup>9</sup></code>
- It is guaranteed that you can make a mountain array out of `nums`.
<hr>

### Hints:
- Think the opposite direction instead of minimum elements to remove the maximum mountain subsequence
- Think of LIS it's kind of close