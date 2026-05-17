from collections import defaultdict


class FreqStack:

    def __init__(self):

        # Store frequency of each number
        #
        # Example:
        # 5 -> 3
        # 7 -> 2
        self.frequency = {}

        # Store stack for each frequency
        #
        # Example:
        #
        # freq_group[1] = [5,7,4]
        # freq_group[2] = [5,7]
        # freq_group[3] = [5]
        #
        self.freq_group = defaultdict(list)

        # Track highest frequency
        self.max_frequency = 0

    def push(self, val):

        # Increase frequency
        self.frequency[val] = (self.frequency.get(val, 0) + 1)
        current_frequency = self.frequency[val]

        # -----------------------------------------
        # Example:
        #
        # push(5)
        #
        # frequency:
        # 5 -> 1
        #
        # freq_group[1] = [5]
        # -----------------------------------------
        self.freq_group[current_frequency].append(val)

        # Update max frequency
        self.max_frequency = max(self.max_frequency,current_frequency)

    def pop(self):

        # -----------------------------------------
        # Pop most recent element
        # from highest frequency stack
        #
        # Example:
        #
        # freq_group[3] = [5]
        #
        # pop -> 5
        # -----------------------------------------
        value = self.freq_group[self.max_frequency].pop()
        # Decrease frequency
        self.frequency[value] -= 1

        # -----------------------------------------
        # If highest frequency stack empty
        #
        # Example:
        #
        # freq_group[3] = []
        #
        # Move max frequency down
        # -----------------------------------------
        if not self.freq_group[self.max_frequency]:
            self.max_frequency -= 1

        return value


# Example run in IntelliJ IDEA / PyCharm
stack = FreqStack()

stack.push(5)
stack.push(7)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(5)

print(stack.pop())  # 5
print(stack.pop())  # 7
print(stack.pop())  # 5
print(stack.pop())  # 4

# Time Complexity:
# push() -> O(1)
# pop()  -> O(1)
#
# Space Complexity: O(N)
#
# N = total pushed elements