num = int(input())

for i in range(num):
    str1 = input()
    str2 = input()
    
    # 대/소문자는 구분하지 않음
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 맨 앞 혹은 맨 뒤에 나오는 공백 괜찮음
    str1 = str1.strip()
    str2 = str2.strip()
    
    # 공백 여러개인것은 괜찮음, 단 유무는 차이가 된다.
    new_str1 = []
    for ch in str1:
        if ch == " " and len(new_str1) > 0 and new_str1[-1] == " ":
            pass
        else:
            new_str1.append(ch)
    str1 = "".join(new_str1)
    
    new_str2 = []
    for ch in str2:
        if ch == " " and len(new_str2) > 0 and new_str2[-1] == " ":
            pass
        else:
            new_str2.append(ch)
    str2 = "".join(new_str2)
    
    # 특수 부호의 바로 앞이나 바로 뒤에 나오는 공백도 있으나 없으나 상관없다.
    special_chrs = [",", ";", ".", ":", "(" ,")", "{", "}", "[", "]"]
    
    new_str1 = []
    for idx, ch in enumerate(str1):
        if ch == " ":
            if idx - 1 >= 0 and str1[idx-1] in special_chrs:
                pass
            elif idx + 1 < len(str1) and str1[idx+1] in special_chrs:
                pass
            else:
                new_str1.append(ch)
        else:
            new_str1.append(ch)
    
    str1 = "".join(new_str1)
            
    new_str2 = []
    for idx, ch in enumerate(str2):
        if ch == " ":
            if idx - 1 >= 0 and str2[idx-1] in special_chrs:
                pass
            elif idx + 1 < len(str2) and str2[idx+1] in special_chrs:
                pass
            else:
                new_str2.append(ch)
                
        else:
            new_str2.append(ch)
    
    str2 = "".join(new_str2)
    
    # 여는 괄호끼리는 종류를 구별하지 않는다.
    str1 = str1.replace("[", "(")
    str1 = str1.replace("{", "(")
    str2 = str2.replace("[", "(")
    str2 = str2.replace("{", "(")
    
    # 닫는 괄호끼리는 종류를 구별하지 않는다.
    str1 = str1.replace("]", ")")
    str1 = str1.replace("}", ")")
    str2 = str2.replace("]", ")")
    str2 = str2.replace("}", ")")
    
    # 쉼표(",")와 세미콜론(";")은 구별하지 않는다.
    str1 = str1.replace(",", ";")
    str2 = str2.replace(",", ";")
    
    if str1 == str2:
        print("Data Set %d: equal\n" % (i+1))
    else:
        print("Data Set %d: not equal\n" % (i+1))
