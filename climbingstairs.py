
###LINKED LIST
##Climbing Stairs.

class Solution(object):
    # Function to calculate the number of ways to climb stairs
    def climbStairs(self, n):
        memo = {}  # Initialize an empty dictionary to store computed results
        return self.ways(n, memo)  # Call the ways method with n and memo as arguments and return the result
    
    # Helper method to calculate the number of ways recursively
    def ways(self, n, memo):
        # Check if the result for n is already computed and stored in memo
        if n in memo:
            return memo[n]  # Return the stored result directly
        
        # Base cases: if n is 1 or 2, return 1 or 2 respectively
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # Recursive case: calculate the result for n by summing up results for n-1 and n-2
        memo[n] = self.ways(n - 1, memo) + self.ways(n - 2, memo)
        return memo[n]  # Store the calculated result in memo and return it


# Time Complexity: O(n), since each value of n is computed only once and stored in the dictionary.
# Space Complexity: O(n), due to the usage of dictionary, which stores the results for each value of n
