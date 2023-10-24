# Removed sort at the beginning. Mess up the duplicate check (== instead of !=). : NSH

'''
Function that sorts a list and removes duplicates
'''
def remove_duplicates(arr):
    unique_arr = []
    removed_elements = []
    # Check if each element if unique, otherwise add it to a list of removed elements
    for i in range(len(arr)):
        if i == 0 or arr[i] == arr[i-1]:
            unique_arr.append(arr[i])
        else:
            removed_elements.append(arr[i])
    return unique_arr, removed_elements

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
# Print the original list, the list with duplicates removed, and the removed elements
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
