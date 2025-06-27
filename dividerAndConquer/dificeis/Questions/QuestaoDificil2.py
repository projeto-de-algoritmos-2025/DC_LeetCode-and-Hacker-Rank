import sys
import threading

def median_of_medians(a):

    n = len(a)
    if n <= 5:
        return sorted(a)[n // 2]

    medians = []
    for i in range(0, n, 5):
        group = a[i:i+5]
        medians.append(sorted(group)[len(group)//2])

    return median_of_medians(medians)

def select(a, k):

    if len(a) == 1:
        return a[0]
    pivot = median_of_medians(a)
    lows  = [x for x in a if x < pivot]
    highs = [x for x in a if x > pivot]
    equals = [x for x in a if x == pivot]
    if k <= len(lows):
        return select(lows, k)
    if k <= len(lows) + len(equals):
        return pivot
    return select(highs, k - len(lows) - len(equals))

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    arr = []
    idx = 1

    for _ in range(n):
        x = int(data[idx]); idx += 1
        arr.append(x)
        m = len(arr)
        if m % 2 == 1:
            mid = select(arr, m//2 + 1)
            print(f"{mid:.1f}")
        else:
            a = select(arr, m//2)
            b = select(arr, m//2 + 1)
            med = (a + b) / 2
            print(f"{med:.1f}")

if __name__ == "__main__":
    
    threading.stack_size(1<<25)
    sys.setrecursionlimit(10**7)
    threading.Thread(target=main).start()