numbers=[0,1,0,4,5]
print(numbers)

"Task 7 of hackerrank"
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]

    print(result)

"Task 8 from hackerank"
"The first line contains n. The second line contains an array a[]  of n integers each separated by a space."
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort()

    print(arr[-2])