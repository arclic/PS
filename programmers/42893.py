# 점수 계산
# html, word, 기본점수, 외부 링크들, 본인 url
def caculatePoint(html, word, basePoint, linkUrls, ownUrl):
    
    alphabet = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    point = 0
    
    # html tag를 기준으로 분리
    seperateTag = []
    tempTag = []
    for char in html:
        if char == ">":
            seperateTag.append(("".join(tempTag)).strip())
            tempTag = []
        elif char == "<":
            seperateTag.append(("".join(tempTag)).strip())
            tempTag = []
        else:
            tempTag.append(char)
    
    externalLinks = []
    
    print(seperateTag)
    
    for tag in seperateTag:
        # 본인 url 계산
        if tag.startswith("meta ") and 'property="og:url"' in tag and "content" in tag:
            url = tag.split('content="')[1]
            ownUrl.append(url[:url.index('"')])
        
        # 외부 url 계산
        elif tag.startswith("a ") and "href" in tag:
            url = tag.split('href="')[1]
            externalLinks.append(url[:url.index('"')])
        
        # 기본 점수 계산
        wordList = [x for x in tag]
        for idx, char in enumerate(wordList):
            # 영어가 아니면 스페이스로 변경
            if char not in alphabet:
                wordList[idx] = " "
        wordList = ("".join(wordList)).split(" ")
        
        for wd in wordList:
            if word == wd:
                point += 1

    linkUrls.append(externalLinks)
    basePoint.append(point)
    

def solution(word, pages):
    answer = 0
    
    word = word.lower()
    
    # 기본 점수
    basePoint = []
    
    # 외부 링크수, 외부 링크들 urls
    numLinks = []
    linkUrls = []
    
    # 본인 url
    ownUrl = []
    
    # 최대값
    maxPoint = 0
    
    for idx, page in enumerate(pages):
        # 대소문자 변경
        page = page.lower()
        
        # 점수계산
        caculatePoint(page, word, basePoint, linkUrls, ownUrl)
    
    for idx1, own in enumerate(ownUrl):
        point = basePoint[idx1]
        for idx2, link in enumerate(linkUrls):
            if own in link:
                point += (basePoint[idx2] / len(linkUrls[idx2]))
                
        if point > maxPoint:
            maxPoint = point
            answer = idx1
    
    return answer
