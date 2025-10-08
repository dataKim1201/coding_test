# 배열의 마지막을 pivot으로 
def quick_sort_visual(arr, depth=0):
    indent = "  " * depth  # 들여쓰기
    if len(arr) <= 1:
        print(f"{indent}반환: {arr}")
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{indent}배열: {arr}")
    print(f"{indent}pivot: {pivot}")
    print(f"{indent} → left: {left}, middle: {middle}, right: {right}\n")
    
    return quick_sort_visual(left, depth + 1) + middle + quick_sort_visual(right, depth + 1)

# 실행
data = [3, 6, 8, 10, 1, 2, 1]
print("최종 결과:", quick_sort_visual(data))
