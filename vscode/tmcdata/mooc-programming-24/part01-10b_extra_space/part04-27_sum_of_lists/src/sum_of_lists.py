# Write your solution here
def list_sum(nums1, nums2):
    sum = []
    count = len(nums1)
    counter = 0
    for x in nums1:
        total = x + nums2[counter]
        sum.append(total)
        counter += 1
    return sum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]