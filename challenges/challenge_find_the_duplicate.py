def find_duplicate(nums):
    """
    Recebe uma lista de números e retorna o número repetido ou False
    caso recebe um valor inválido ou lista sem números repetidos
    """

    if not isinstance(nums, list):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        num = nums[i]
        if not isinstance(num, int) or num < 0:
            return False
        if num == nums[i + 1]:
            return num

    return False
