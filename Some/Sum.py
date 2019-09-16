def calc(num, nums = []):
	for i in range(len(nums)):
		
		for j in range(len(nums)):
			if j != i and num - nums[i] == nums[j]:
				return True
	return False

def calc1(num, nums = []):
	for i in range(len(nums)):

		for j in range(len(nums)):
			if j != i and nums[i] + nums[j] == num:
				return True
	return False


print(calc(10, [5, 5]))
print(calc1(10, [5, 5]))