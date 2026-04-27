def remove_duplicates(sorted_list):
    
    if len(sorted_list) == 0:
        return []

    
    unique_list = [sorted_list[0]]

   
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            unique_list.append(sorted_list[i])

    return unique_list



nums = [1, 1, 2, 2, 3, 4, 4, 5]

print("Original List:", nums)


result = remove_duplicates(nums)

print("List after removing duplicates:", result)
