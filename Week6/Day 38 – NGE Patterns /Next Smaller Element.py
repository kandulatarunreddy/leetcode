class Solution:
    def nextSmallerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []  # stack stores indices

        for i in range(n):

            # If current element is smaller than stack top,
            # it is the next smaller for that index
            while stack and arr[i] < arr[stack[-1]]:
                index = stack.pop()
                result[index] = arr[i]

            stack.append(i)

        return result


if __name__ == "__main__":
    arr = [4, 8, 5, 2, 25]

    sol = Solution()
    ans = sol.nextSmallerElement(arr)

    print("Input:", arr)
    print("Next Smaller Elements:", ans)

# TC: O(n)  SC: O(n)