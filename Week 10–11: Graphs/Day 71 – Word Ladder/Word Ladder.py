from collections import defaultdict, deque

def word_ladder_length(beginWord, endWord, wordList):
    # Step 1: If endWord is not in dictionary → no solution
    if endWord not in wordList:
        return 0

    # Step 2: Preprocess words into pattern dictionary
    # pattern_dict maps generic patterns → list of matching words
    pattern_dict = defaultdict(list)

    wordList.append(beginWord)  # include beginWord for pattern generation

    for word in wordList:
        for i in range(len(word)):
            # Create pattern by replacing one character with '*'
            pattern = word[:i] + '*' + word[i+1:]
            pattern_dict[pattern].append(word)

    # Step 3: BFS initialization
    queue = deque([(beginWord, 1)])  # (current_word, steps)
    visited = set([beginWord])

    # Step 4: BFS traversal
    while queue:
        current_word, level = queue.popleft()

        # If we reached the target → return steps
        if current_word == endWord:
            return level

        # Step 5: Generate neighbors using patterns
        for i in range(len(current_word)):
            pattern = current_word[:i] + '*' + current_word[i+1:]

            # Get all words that share this pattern
            for neighbor in pattern_dict[pattern]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

            # 🔥 Important optimization:
            # Clear the list so we don't process it again
            pattern_dict[pattern] = []

    return 0
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    result = word_ladder_length(beginWord, endWord, wordList)

    print("Shortest transformation length:", result)


# Time Complexity: O(N * L^2)
# Space Complexity: O(N * L)
'''🧩 One-line intuition
Brute force = “try everything and filter”
Pattern BFS = “jump directly to valid neighbors”
🏁 Final conclusion

👉 You are 100% correct mathematically:

Pattern BFS has O(N × L²), which is worse than O(N × L)

BUT:

It is still preferred because it drastically reduces real-world search space and is the standard interview solution.
'''

'''
| Step | Queue Before      | Current Word | Level | Patterns          | Neighbors Added | Queue After       | Visited                             |
| ---- | ----------------- | ------------ | ----- | ----------------- | --------------- | ----------------- | ----------------------------------- |
| 1    | [(hit,1)]         | hit          | 1     | `*it`,`h*t`,`hi*` | hot             | [(hot,2)]         | {hit, hot}                          |
| 2    | [(hot,2)]         | hot          | 2     | `*ot`,`h*t`,`ho*` | dot, lot        | [(dot,3),(lot,3)] | {hit, hot, dot, lot}                |
| 3    | [(dot,3),(lot,3)] | dot          | 3     | `*ot`,`d*t`,`do*` | dog             | [(lot,3),(dog,4)] | {hit, hot, dot, lot, dog}           |
| 4    | [(lot,3),(dog,4)] | lot          | 3     | `*ot`,`l*t`,`lo*` | log             | [(dog,4),(log,4)] | {hit, hot, dot, lot, dog, log}      |
| 5    | [(dog,4),(log,4)] | dog          | 4     | `*og`,`d*g`,`do*` | cog             | [(log,4),(cog,5)] | {hit, hot, dot, lot, dog, log, cog} |
| 6    | [(log,4),(cog,5)] | log          | 4     | `*og`,`l*g`,`lo*` | — (all visited) | [(cog,5)]         | unchanged                           |
| 7    | [(cog,5)]         | cog          | 5     | —                 | ✅ FOUND         | —                 | —                                   |
'''