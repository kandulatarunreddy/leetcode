from collections import defaultdict, deque


def alienOrder(words):
    # -----------------------------
    # Step 1: Initialize graph
    # -----------------------------
    adj = defaultdict(set)   # adjacency list
    indegree = {}            # count of incoming edges

    # Initialize all unique characters
    for word in words:
        for c in word:
            indegree[c] = 0 #We must include ALL characters, even those with: no incoming edges, no outgoing edges

    # -----------------------------
    # Step 2: Build graph
    # -----------------------------
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]

        # Edge case: invalid order like ["abc","ab"]
        '''
        ❌ Why invalid?
        Dictionary says: "abc" comes BEFORE "ab"
        But logically:   "ab" should come before "abc"    
        👉 This violates lexicographical order   '''
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        # Find first different character
        '''
        words = ["wrt", "wrf"]
        | Index | w1 | w2  |
        | ----- | -- | --- |
        | 0     | w  | w   |
        | 1     | r  | r   |
        | 2     | t  | f ❗|
        
        

        '''
        for j in range(min(len(w1), len(w2))):
            # j = 0 → w == w → skip
            # j = 1 → r == r → skip
            # j = 2 → t != f → FIRST DIFFERENCE
            if w1[j] != w2[j]:
                # -----------------------------
                # RULE: t must come before f
                # -----------------------------

                # Add edge t → f
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j]) # adj['t'].add('f')
                    # Increase indegree of 'f'
                    indegree[w2[j]] += 1    # indegree['f'] += 1
                break

    # -----------------------------
    # Step 3: Topological Sort (BFS)
    # -----------------------------
    queue = deque()

    # Add all nodes with 0 indegree
    for c in indegree:
        if indegree[c] == 0:
            queue.append(c)

    result = []

    while queue:
        char = queue.popleft()
        result.append(char)

        for nei in adj[char]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    # -----------------------------
    # Step 4: Check for cycle
    # -----------------------------
    #result = "wertf"
    #indegree size = 5
    '''
    words = ["z", "x", "z"]
    z ↔ x   (cycle)
    indegree:: z:1, x:1
    No node has indegree 0 ❌
    queue = []
    result = ""
    len(result) = 0
    len(indegree) = 2   
    '''
    if len(result) != len(indegree):
        return ""  # cycle detected

    return "".join(result)


# -----------------------------
# Driver Code (for IntelliJ run)
# -----------------------------
if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]

    order = alienOrder(words)

    print("Alien Dictionary Order:", order)


# Time Complexity: O(N * L + K)
# Space Complexity: O(K)