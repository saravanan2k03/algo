nums1 = [1,3]
nums2 = [2,4]
arr3 =[]
# while nums1 and nums2:
#     if nums1[0] <= nums2[0]:
#         arr3.append(nums1.pop(0))
#     else:
#         arr3.append(nums2.pop(0))
# while nums1:
#    arr3.append(nums1.pop(0))
# while nums2:
#    arr3.append(nums2.pop(0))

# mid = len(arr3) //2
# if len(arr3) % 2 !=0:
#     print(arr3[mid])
# else:
#     print((float(arr3[mid]+arr3[mid-1]))/2)



nums1.extend(nums2)
nums1.sort()
mid = len(nums1) // 2
if len(nums1) % 2 != 0:
    print(nums1[mid])
else:
    print((float(nums1[mid]+nums1[mid-1]))/2)
    