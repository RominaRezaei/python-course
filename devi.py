def sum(x1,x2):
    result_s={}
    result_s["n"]=(x1["n"]*x2["n"]) + (x2["n"]*x2["d"])
    result_s["d"]=x1["d"]*x2["d"]
    return result_s

def multyply(f1,f2):
    result_m={}
    result_m['n']=f1["n"]*f2["d"]
    result_m['d']=f1["d"]*f2["n"]
    return result_m

def min(f1,f2):
    result_mi={}
    result_mi["n"]=(f1["n"]*f2["d"]) - (f2["n"]*f2["d"])
    result_mi["d"]=f1["d"]*f2["d"]
    return result_mi

def div(x1, x2 ):
    result_mi={}
    result_mi["n"]=(x1["n"]*x2["d"])
    result_mi["d"]=x1["d"]*x2["n"]
    return result_mi

def show(r):
    print(f"{r['n']} / {r['d']}")

x1={"n":2 , "d":3}
x2={"n":5 , "d":4}


result_n=sum(x1,x2)
show(result_n)
result_d=multyply(x1,x2)
show(result_d)
result_mi=min(x1,x2)
show(result_mi)
result_d=div(x1,x2)
show(result_d)
