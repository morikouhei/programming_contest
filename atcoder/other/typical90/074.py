n = int(input())
dic = {"a":0, "b":1, "c":2}
print(sum([dic[s]*pow(2,i) for i,s in enumerate(input())]))