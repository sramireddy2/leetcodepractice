class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = []
        curr = 0
        for num in nums:
            curr += num
            self.prefixsum.append(curr)
        
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.prefixsum[right]
        leftsum = self.prefixsum[left - 1] if left > 0 else 0
        return rightsum - leftsum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)