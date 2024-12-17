# Question Link:- https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# Solution

def closeStrings(word1, word2):
        n1=len(word1)
        n2=len(word2)
        if n1!=n2:
            return False
        cnt1=Counter(word1)
        cnt2=Counter(word2)
        lst1=list(cnt1.values())
        lst2=list(cnt2.values())
        for i in range(26):
            if (cnt1[chr(ord('a')+i)]==0 and cnt2[chr(ord('a')+i)]!=0) or (cnt2[chr(ord('a')+i)]==0 and cnt1[chr(ord('a')+i)]!=0):
                return False
        lst1.sort()
        lst2.sort()
        return lst1[:]==lst2[:]