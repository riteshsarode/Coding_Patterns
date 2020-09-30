# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only refruitsiction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# Solution: This problem follows the Sliding Window pattern and is quite similar to Longest Subfruitsing with K Distinct Characters. 
# In this problem, we need to find the length of the longest subarray with no more than two distinct characters (or fruit types!). 
# This transforms the current problem into Longest Subfruitsing with K Distinct Characters where K=2.

import collections

def fruits_into_baskets(fruits):
  start = 0
  max_length = 0
  char_frequency = collections.defaultdict(int) # Defaults new value to 0

  # in the following loop we'll try to extend the range [start, end]
  for end in range(len(fruits)):
    right_char = fruits[end]
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(char_frequency) > 2:
      left_char = fruits[start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, end - start + 1)
  return max_length

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()
# Time Complexity: O(N) in best case. In worst case O(Nk)
# Space Complexity: O(k)