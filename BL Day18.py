def find_subarray(arr, sum):
   """
   Finds the subarray with a given sum in an array of integers.

   Args:
       arr: The array of integers.
       sum: The target sum.

   Returns:
       A list containing the starting and ending indices of the subarray,
       or None if no subarray is found.
   """

   current_sum = 0
   start = 0

   for i, num in enumerate(arr):
       current_sum += num

       while current_sum > sum:
           current_sum -= arr[start]
           start += 1

       if current_sum == sum:
           return [start, i]

   return None

# Get input from the user
arr_str = input("Enter the array of integers separated by spaces: ")
arr = [int(num) for num in arr_str.split()]  # Convert string input to a list of integers
target_sum = int(input("Enter the target sum: "))

# Find the subarray
result = find_subarray(arr, target_sum)

if result:
   print("Subarray found from index", result[0], "to", result[1])
else:
   print("No subarray found with the given sum")
