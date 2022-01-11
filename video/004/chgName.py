import os 
"""
os = 파이썬 내의 모듈
폴더 관련 파일 윈도우즈 시스템 관련
"""

for i in os.listdir('./'):
    
    print(i + '==>' + i.replace("어려운 경제를 쉽고 재밌게! ","cider_"))
    os.rename(i, i.replace("어려운_경제를_쉽고_재밌게!_","cider_"))