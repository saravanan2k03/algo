nums1 = [1,3]
nums2 = [2,4]
res = []
nums1.extend(nums2)
nums1.sort()
print(nums1)
print(len(nums1))
while len(nums1) != 2:
        nums1.pop(0)
        nums1.pop()
print(nums1)
n= len(nums1)
print(n)

