arr = [int(part) for part in input().split()]
target = int(input())

# vet can
def two_num(arr, target):
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
# Độ phức tạp:
#   Thời gian: 2 vòng lặp lồng nhau -> O(n^2)
#   Không gian: chỉ sử dụng các biến đơn giản -< O(1)

#cach 2
def two_num_hashmap(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return []

# Độ phức tạp
#   Thời gian: 1 vòng lặp -> O(n)
#   Không gian: dùng 1 map -> O(n)

print(hashmap(arr,target))