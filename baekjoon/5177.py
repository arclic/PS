import sys
import re

num = int(input())

for i in range(num):
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    
    # 대문자와 소문자 구분이 없다.
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 공백의 개수는 상관이 없다. + 문자열의 맨 앞 혹은 맨 뒤에 나타나는 공백은 있으나 없으나 관계없다.
    str1 = re.sub("[ ]+"," ", str1).strip()
    str2 = re.sub("[ ]+"," ", str2).strip()
    
    # 특수 부호의 바로 앞이나 바로 뒤에 나오는 공백도 있으나 없으나 상관없다.
    str1 = re.sub("[ ]?[(){}\[\].,;:][ ]?", lambda m : str(m.group()).strip(), str1)
    str2 = re.sub("[ ]?[(){}\[\].,;:][ ]?", lambda m : str(m.group()).strip(), str2)
    
    # 여는 괄호끼리는 종류를 구별하지 않는다.
    str1 = re.sub("[{(\[]", "(", str1)
    str2 = re.sub("[{(\[]", "(", str2)
    
    # 닫는 괄호끼리는 종류를 구별하지 않는다.
    str1 = re.sub("[})\]]", ")", str1)
    str2 = re.sub("[})\]]", ")", str2)
    
    # 쉼표(",")와 세미콜론(";")은 구별하지 않는다.
    str1 = re.sub(",", ";", str1)
    str2 = re.sub(",", ";", str2)
    
    if str1 == str2:
        print("Data Set %d: equal\n" % (i+1))
    else:
        print("Data Set %d: not equal\n" % (i+1))
