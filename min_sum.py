def miniMaxSum(arr):
    total = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    print(f"{total - max_val} {total - min_val}")


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    miniMaxSum(arr)
