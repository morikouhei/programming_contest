t = int(input())
for _ in range(t):
    s = input()
    ze = s.count("0")
    on = len(s)-ze
    print("DA" if min(on,ze)%2 else "NET")