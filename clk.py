def sum(time1, time2):
    result = {}
    result["hour"] = time1["hour"] + time2["hour"]
    result["min"] = time1["min"] + time2["min"]
    result["sec"] = time1["sec"] + time2["sec"]
    if result["sec"]>=60:
        result["sec"]-= 60
        result["min"]+= 1
    
    if result["min"] >= 60:
        result["min"]-= 60
        result["hour"]+= 1
    return result

def subtraction(s1, s2):
    result = {}
    result["hour"] = s2["hpur"] - s1["hour"]
    result["min"] = s2["min"] - s1["min"]
    result["sec"] = s2["sec"] - s1["sec"]
    if result["sec"] < 0:
       result["min"] -= 1
       result["hour"] += 60

    if result["min"] < 0:
       result["hour"] -=1
       result["sec"] +=60

    if result["hour"] < 0:
        print("not defined")

    return result


def show(result):
    print(f"{result['hour']} : {result['min']} : {result['sec']}")

s1 = {"hour": int(input("time1: ")), "min": int(input("time1: ")) , "sec": int(input("time1: "))}
s2 = {"hour": int(input("time2: ")) , "min": int(input("time2: ")) , "sec": int(input("time2: "))}
result_s = sum(s1,s2)
show(result_s)
result_m = subtraction(s1,s2)
show(subtraction)
