if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort();
    a = max(arr);
    while max(arr) == a:
        arr.remove(max(arr))
    print(max(arr))