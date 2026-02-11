class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, no permutation can exist
        if len(s1) > len(s2):
            return False
        # Frequency arrays for 26 lowercase letters
        s1Count, s2Count = [0] * 26, [0] * 26

        # Build initial window of size len(s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # matches = how many characters (out of 26) currently match in frequency
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        # Slide the window across s2
        for r in range(len(s1), len(s2)):

            # If all 26 chars match, we found a permutation
            if matches == 26:
                return True
            # ---------------------------------------------------
            # 1) ADD the new character entering the window (right side)
            # ---------------------------------------------------
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # After adding this char, check how "matches" changes.
            # We only care about this ONE character's frequency change.
            if s1Count[index] == s2Count[index]:
                # We just made the counts equal -> gained a match
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                # Before adding, counts were equal.
                # Now s2 has ONE extra -> lost a match.
                matches -= 1

            # ---------------------------------------------------
            # 2) REMOVE the character leaving the window (left side)
            # ---------------------------------------------------
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # WHY we do this:
            # The sliding window moved forward by 1.
            # So the leftmost character is no longer inside the window.
            # We must subtract its frequency from s2Count.
            if s1Count[index] == s2Count[index]:
                # After removing, counts became equal -> gained a match
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                # Before removing, counts were equal.
                # Now s2 has ONE LESS -> lost a match.
                matches -= 1
            l += 1
        return matches == 26

sol=Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1,s2))
#Tc:O(n) Sc:O(1)

