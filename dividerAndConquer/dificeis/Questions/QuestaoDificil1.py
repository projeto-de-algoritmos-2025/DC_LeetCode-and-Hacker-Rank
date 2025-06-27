import sys

def median_of_medians(a):

    n = len(a)
    if n <= 5:
        return sorted(a)[n//2]
    
    medians = []
    for i in range(0, n, 5):
        chunk = a[i:i+5]
        medians.append(sorted(chunk)[len(chunk)//2])

    return median_of_medians(medians)

def select(a, k):
 
    if len(a) == 1:
        return a[0]
    pivot = median_of_medians(a)
    lows  = [x for x in a if x < pivot]
    highs = [x for x in a if x > pivot]
    mids  = [x for x in a if x == pivot]
    if k <= len(lows):
        return select(lows, k)
    elif k <= len(lows) + len(mids):
        return pivot
    else:
        return select(highs, k - len(lows) - len(mids))

def print_median(arr):
    if not arr:
        print("Wrong!")
        return
    m = len(arr)
    if m % 2 == 1:
        
        v = select(arr, m//2 + 1)
        print(v)
    else:
       
        a = select(arr, m//2)
        b = select(arr, m//2 + 1)
        s = a + b
        if s % 2 == 0:
            print(s//2)
        else:
            
            print(f"{s/2:.1f}".rstrip('0').rstrip('.'))

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    arr = []
    idx = 1
    for _ in range(n):
        op = data[idx]; x = int(data[idx+1])
        idx += 2
        if op == 'a':
            arr.append(x)
            print_median(arr)
        else:  
            if x in arr:
                arr.remove(x)
                print_median(arr)
            else:
                print("Wrong!")

if __name__ == "__main__":
    main()