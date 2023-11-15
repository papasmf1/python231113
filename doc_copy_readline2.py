import re  # 특정한 패턴을 찾아주는 도구인 're'를 가져와요.

# 'PV3.txt'라는 파일을 텍스트 읽기 모드로 열고, 다른 파일 'PV3_copy.txt'를 UTF-8 인코딩으로 텍스트 쓰기 모드로 열어요.
f = open('PV3.txt', 'rt')
g = open('PV3_copy.txt', 'wt', encoding='utf-8')

# 파일 'PV3.txt'의 첫 줄을 읽어요.
line = f.readline()

# 파일에서 읽을 줄이 있을 때까지:
while (line != ''):  # 줄이 비어있지 않은 동안:
    # 그 줄에 "error"라는 단어가 있는지 확인해요.
    if (re.search("error", line)):  # 만약 그 줄에 "error"라는 단어가 있다면:
        # 그 줄을 파일 'PV3_copy.txt'에 씁니다.
        g.write(line + "\n")
    
    # 파일 'PV3.txt'에서 다음 줄을 읽어요.
    line = f.readline()

# 작업이 끝나면 파일을 닫아요.
f.close()
g.close()









