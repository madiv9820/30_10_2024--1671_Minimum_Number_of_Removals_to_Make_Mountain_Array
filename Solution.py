from typing import List
import sys

class Solution:
    # Helper function to calculate the Longest Increasing Subsequence (LIS) up to each index
    def __longest_Increasing_Subsequence(self, nums: List[int]) -> List[int]:
        # Initialize the LIS array where each element will store the length of the 
        # longest increasing subsequence that ends at that index.
        LIS = [0] * self.__length
        LIS[0] = 1  # The LIS for the first element is always 1 (only that element itself)
        
        # Loop through each index from 1 to end of nums
        for current_Index in range(1, self.__length):
            # Variable to keep track of the max subsequence length found so far for LIS at current_Index
            max_Increasing_Subsequence = 0
            
            # Inner loop to check all elements before current_Index
            for index in range(current_Index):
                # Check if we have a strictly increasing subsequence
                if nums[index] < nums[current_Index]:
                    # Update the maximum LIS length that can be achieved at current_Index
                    max_Increasing_Subsequence = max(max_Increasing_Subsequence, LIS[index])
            
            # Add 1 to the longest subsequence length found so far to include the current element
            LIS[current_Index] = 1 + max_Increasing_Subsequence

        # Return the LIS array containing LIS length up to each index
        return LIS
    
    # Helper function to calculate the Longest Decreasing Subsequence (LDS) from each index
    def __longest_Decreasing_Subsequence(self, nums: List[int]) -> List[int]:
        # Initialize the LDS array where each element will store the length of the 
        # longest decreasing subsequence that starts at that index.
        LDS = [0] * self.__length
        LDS[self.__length-1] = 1  # The LDS for the last element is always 1 (only that element itself)

        # Loop backwards through nums from the second-to-last element to the first
        for current_Index in range(self.__length-2, -1, -1):
            # Variable to track the max subsequence length found so far for LDS at current_Index
            max_Decreasing_Subsequence = 0
            
            # Inner loop to check all elements after current_Index
            for index in range(self.__length-1, current_Index, -1):
                # Check if we have a strictly decreasing subsequence
                if nums[index] < nums[current_Index]:
                    # Update the maximum LDS length that can be achieved at current_Index
                    max_Decreasing_Subsequence = max(max_Decreasing_Subsequence, LDS[index])
            
            # Add 1 to the longest subsequence length found so far to include the current element
            LDS[current_Index] = 1 + max_Decreasing_Subsequence
        
        # Return the LDS array containing LDS length from each index
        return LDS

    # Main function to calculate the minimum number of removals to form a mountain array
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Set the length of nums as an instance variable
        self.__length = len(nums)

        # Obtain LIS and LDS arrays to determine the mountain structure for each element
        LIS = self.__longest_Increasing_Subsequence(nums)
        LDS = self.__longest_Decreasing_Subsequence(nums)

        # Initialize the minimum removals to a large number (infinity)
        minimum_Removals = sys.maxsize

        # Loop over each element except the first and last (mountain peak should not be at the edges)
        for index in range(1, self.__length-1):
            # Check if the current element can serve as a peak in a mountain (LIS and LDS must be > 1)
            if LIS[index] > 1 and LDS[index] > 1:
                # Calculate removals required on the left side (to make it strictly increasing up to peak)
                left_Side_Remove_Count = (index) - (LIS[index] - 1)
                # Calculate removals required on the right side (to make it strictly decreasing after peak)
                right_Side_Remove_Count = (self.__length - index - 1) - (LDS[index] - 1)
                
                # Update the minimum removals required to form a mountain
                minimum_Removals = min(minimum_Removals, left_Side_Remove_Count + right_Side_Remove_Count)

        # Return the minimum number of removals found to form the mountain array
        return minimum_Removals