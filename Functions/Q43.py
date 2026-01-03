# Find the maximum value in a list:
def maxn(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    maxr = maxn(numbers[1:])
    return numbers[0] if numbers[0] > maxr else maxr

li = [560,39,580,478,577]
print(maxn(li))