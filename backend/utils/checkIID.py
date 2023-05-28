import time
import datetime

coeff = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

def checkIID(ID: str) -> int:
    today = datetime.datetime.now().strftime('%Y%m%d')
    year = time.localtime(time.time())[0]
    if len(ID) != 18:
        return 0
    if not ID[0:17].isdigit():
        return 0
    if int(ID[6:10]) not in range(1900, year + 1):
        return 0
    if int(ID[6:14]) > int(today):
        return 0
    try:
        time.strptime(ID[6:14], "%Y%m%d")
        tmp = 0
        for i in range(0, 17):
            tmp = tmp + int(ID[i]) * coeff[i]
        mod = tmp % 11
        if str(check[mod]) == ID[-1]:
            return 1
        else:
            return 0
    except:
        return 0
            
# ref: https://blog.csdn.net/hynet365/article/details/127276003