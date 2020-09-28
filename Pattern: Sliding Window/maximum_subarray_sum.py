# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

## Brute force solution is to calculate window sum for each starting index
## Time Complexity: O(N * K) Where N=> Length of arr, K=> window size
def max_sub_array_of_size_k(k, arr):
  max_sum = 0
  window_sum = 0

  for i in range(len(arr) - k + 1):
    window_sum = 0
    for j in range(i, i+k):
      window_sum += arr[j]
    max_sum = max(max_sum, window_sum)
  return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()


## Optimized solution can be derived by considering each subarray as a Sliding Window of size ‘k’.
## Time Complexity: O(N)
def max_sub_array_of_size_k(k, arr):
  subarray_start = 0
  running_sum = 0
  max_sum = 0

  for index in range(len(arr)):
    running_sum += arr[index]
    if index - subarray_start +1 > k:     # slide the window, we don't need to slide if we've not hit the required window size of 'k'
      running_sum -= arr[subarray_start]  # subtract the element going out
      subarray_start += 1                 # slide the window ahead
      max_sum = max(max_sum, running_sum)
    print(running_sum)
  
  return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()