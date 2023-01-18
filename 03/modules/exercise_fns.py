def summary(nums):
    list_sum = sum(nums)
    return (list_sum, list_sum / len(nums), min(nums), max(nums))

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def hist(dictionary):
    result = {}
    for v in dictionary.values():
        if v in result:
            result[v] += 1
        else:
            result[v] = 1
    return result
