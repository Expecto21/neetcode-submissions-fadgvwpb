class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        

        while low<high:
            mid=(low+high)//2
            if nums[high]<nums[mid]:
                low=mid+1
            else:
                high=mid


        pivot=low
        low=0
        high=len(nums)-1

        if target>=nums[pivot] and target<=nums[high]:
            low = pivot
        else:
            high=pivot-1

        
        while low<=high:
            mid=(low+high)//2

            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
            
        return -1

        