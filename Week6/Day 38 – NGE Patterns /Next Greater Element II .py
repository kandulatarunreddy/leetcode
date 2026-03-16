class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)

        # Result array initialized with -1
        # Default assumption: no greater element exists
        result = [-1] * n

        # Stack will store indices of elements
        stack = []

        # We traverse the array twice to simulate circular behavior
        for i in range(2 * n):

            # Current number (use modulo for circular index)
            current = nums[i % n]

            # If current element is greater than the element
            # at index stored on stack top, we found the next greater element
            while stack and nums[stack[-1]] < current:
                index = stack.pop()
                result[index] = current

            # Only push indices during the first pass
            # Second pass is only to resolve remaining elements
            if i < n:
                stack.append(i)

        return result


if __name__ == "__main__":
    nums = [1, 2, 1]

    sol = Solution()
    ans = sol.nextGreaterElements(nums)

    print("Input:", nums)
    print("Next Greater Elements:", ans)

# TC: O(n)  SC: O(n)