class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        # Traverse nums2 to build next greater map
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Elements left in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build result for nums1
        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result


if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    sol = Solution()
    output = sol.nextGreaterElement(nums1, nums2)

    print("nums1:", nums1)
    print("nums2:", nums2)
    print("Next Greater Elements:", output)

# TC: O(n + m), SC: O(n)