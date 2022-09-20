def bubblesort(nums):
    nums1=list(nums)
    for j in range(len(nums1)-1):
        for i in range(len(nums1)-1):
            if nums1[i]>nums1[i+1]:
                nums1[i],nums1[i+1]=nums1[i+1],nums1[i]
    
    return nums1

print(bubblesort([8,3,4,9,1]))

def insertionsort(nums):
    nums2=list(nums)
    for i in range(len(nums2)):
        cur=nums2.pop(i)
        j=i-1
        while j>=0 and nums2[j]>cur:
            j-=1
        nums2.insert(j+1,cur)

    return nums2

print(insertionsort([8,3,4,9,1]))

def merge(nums1,nums2):
    merged=[]
    i,j=0,0

    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1

        nums1_tail=nums1[i:]
        nums2_tail=nums2[j:]

    finalmerge=merged+nums1_tail+nums2_tail
    return finalmerge

# Merge sort
def merge_sort(nums):
    if len(nums)<=1:
        return nums

    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]

    left_sorted,right_sorted=merge_sort(left),merge_sort(right)

    sorted_nums=merge(left_sorted,right_sorted)
    return sorted_nums

print(merge_sort([8,3,4,9,1]))


def partition(nums,start=0,end=None):
    if end is None:
        end=len(nums)-1

    l,r=start,end-1
    while r>l:
        if nums[l]<=nums[end]:
            l+=1
        elif nums[r]>nums[end]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]

    if nums[l]>nums[end]:
        nums[l],nums[end]=nums[end],nums[l]
        return l
    else:
        return end

# Quick sort
def quicksort(nums,start=0,end=None):
    if end is None:
        nums=list(nums)
        end=len(nums)-1

    if start<end:
        pivot=partition(nums,start,end)
        quicksort(nums,start,pivot-1)
        quicksort(nums,pivot+1,end)

    return nums

print(quicksort([8,3,4,9,1]))