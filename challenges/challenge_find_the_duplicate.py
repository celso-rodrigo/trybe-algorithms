def find_duplicate(nums):
    """Faça o código aqui."""
    if not nums or not isinstance(nums, list):
        return False

    unique_nums = []
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        elif num in unique_nums:
            return num
        else:
            unique_nums.append(num)
    return False
