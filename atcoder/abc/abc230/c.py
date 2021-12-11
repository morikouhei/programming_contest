n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

la = max(1-a,1-b)
ra = min(n-a,n-b)

lb = max(1-a,b-n)
rb = min(n-a,b-1)
for i in range(p,q+1):
    st = []
    for j in range(r,s+1):
        da = i-a
        db = j-b
        if da == db and la <= da <= ra:
            st.append("#")
        elif da == -db and lb <= da <= rb:
            st.append("#")
        else:
            st.append(".")
    print(*st,sep="")