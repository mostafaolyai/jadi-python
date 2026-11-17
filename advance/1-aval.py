def divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

ls=[]
d=[]
res = None
max_divisors = 0

for i in range(3):
    inp = int(input())
    ls.append(int(inp))

    div_len = divisors(inp)

    if div_len > max_divisors:
        max_divisors = div_len
        d.append((inp,div_len))

print(f"c : {d}")

if len(d)==0 or len(d)==1:
    print(f"Result1 : {d}")
else:
    d.sort(key=lambda x: x[0], reverse=True)
    print(f"sort : {d}")
    max_second = max(item[1] for item in d)
    filtered = [item for item in d if item[1] == max_second]
    print(f"Result2 : {filtered[0]}")
