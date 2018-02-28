def helper(nums, target, cur, cache):
    key = str((cur, target))
    if key in cache:
        return cache[key]
    if target < 0:
        return False
    if target == 0:
        return True
    if not nums:
        return False

    for i in xrange(len(nums)):
        cur.append(nums[i])
        if helper(nums[:i] + nums[i+1:], target - nums[i], cur, cache):
            cache[key] = True
            return cache[key]
        cur.pop()

    cache[key] = False
    return cache[key]

def subset_sum(nums, target):
    cache = {}
    nums.sort()
    return helper(nums, target, [], cache)

print subset_sum([3, 34, 4, 12, 5, 2], 9) # returns (5, 4)
