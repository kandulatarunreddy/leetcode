from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    """
    Returns ALL shortest transformation sequences from beginWord to endWord.
    Each transformation changes exactly one letter and must exist in wordList.
    """

    # -----------------------------
    # Step 1: Edge case check
    # -----------------------------
    if endWord not in wordList:
        return []

    # Add beginWord to dictionary for pattern building
    wordList.append(beginWord)

    # -----------------------------
    # Step 2: Build pattern dictionary
    # Example:
    # hot -> *ot, h*t, ho*
    # *ot -> [hot, dot, lot]
    # -----------------------------
    pattern_dict = defaultdict(list)

    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_dict[pattern].append(word)

    # -----------------------------
    # Step 3: BFS to build shortest path graph
    # We store:
    # parents[child] = all possible previous words (shortest path only)
    # -----------------------------
    parents = defaultdict(list)

    queue = deque([beginWord])
    visited = set([beginWord])

    found = False  # becomes True when we first reach endWord

    while queue and not found:

        # Nodes visited in this BFS level
        local_visited = set()

        # Process current BFS level
        for _ in range(len(queue)):
            word = queue.popleft()

            # Try changing each character
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]

                # Check all words matching this pattern
                for neighbor in pattern_dict[pattern]:

                    # Only consider unvisited nodes
                    if neighbor not in visited:

                        # Add neighbor to next level only once
                        if neighbor not in local_visited:
                            local_visited.add(neighbor)
                            queue.append(neighbor)

                        # Store parent relationship (for path reconstruction)
                        parents[neighbor].append(word)

                        # If we reach endWord, stop BFS at this level
                        if neighbor == endWord:
                            found = True

        # Mark all nodes in this level as visited
        visited.update(local_visited)

    # -----------------------------
    # Step 4: If no path found
    # -----------------------------
    if not found:
        return []

    # -----------------------------
    # Step 5: Backtracking (DFS)
    # Reconstruct all shortest paths from endWord → beginWord
    # -----------------------------
    result = []

    def dfs(word, path):
        # Base case: reached start
        if word == beginWord:
            result.append(path[::-1])  # reverse path
            return

        # Explore all parents of current word
        for p in parents[word]:
            dfs(p, path + [p])

    # Start DFS from endWord
    dfs(endWord, [endWord])

    return result

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    print(findLadders(beginWord, endWord, wordList))

'''
🚀 Step 1: BFS + Parent Building (Level-wise)
We stop BFS as soon as we reach cog at the first shortest level.


| Level | Queue Before | Current Word | Patterns Used | Neighbors Found | Parents Updated  | Queue After | Visited (level-wise) |
| ----- | ------------ | ------------ | ------------- | --------------- | ---------------- | ----------- | -------------------- |
| 1     | [hit]        | hit          | *it, h*t, hi* | hot             | hot←hit          | [hot]       | {hot}                |
| 2     | [hot]        | hot          | *ot, h*t, ho* | dot, lot        | dot←hot, lot←hot | [dot, lot]  | {dot, lot}           |
| 3     | [dot, lot]   | dot          | *ot, d*t, do* | dog             | dog←dot          | [lot, dog]  | {dog}                |
| 3     | [lot, dog]   | lot          | *ot, l*t, lo* | log             | log←lot          | [dog, log]  | {log}                |
| 4     | [dog, log]   | dog          | *og, d*g, do* | cog             | cog←dog          | [log]       | {cog}                |
| 4     | [log]        | log          | *og, l*g, lo* | cog             | cog←log          | []          | {cog}                |

🧩 Parent Graph Built
After BFS completes:
hot → hit
dot → hot
lot → hot
dog → dot
log → lot
cog → dog, log

🧭 Step 2: DFS Backtracking

Now we build paths from cog → hit.
📊 DFS Backtracking Table
| Step | Current Node | Path So Far (reversed)    | Action                    |
| ---- | ------------ | ------------------------- | ------------------------- |
| 1    | cog          | [cog]                     | start                     |
| 2    | dog          | [cog, dog]                | parent of cog             |
| 3    | dot          | [cog, dog, dot]           | parent of dog             |
| 4    | hot          | [cog, dog, dot, hot]      | parent of dot             |
| 5    | hit          | [cog, dog, dot, hot, hit] | reached start → save path |

🔁 Backtracking Second Path
| Step | Current Node | Path                      |
| ---- | ------------ | ------------------------- |
| 1    | cog          | [cog]                     |
| 2    | log          | [cog, log]                |
| 3    | lot          | [cog, log, lot]           |
| 4    | hot          | [cog, log, lot, hot]      |
| 5    | hit          | [cog, log, lot, hot, hit] |
🎯 Final Answer (Reversed Paths)
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
'''