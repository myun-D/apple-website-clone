import os 
"""
os = 파이썬 내의 모듈
폴더 관련 파일 윈도우즈 시스템 관련
"""

for i in os.listdir('./'):
    
    print(i + '==>' + i.replace(" ","_"))
    os.rename(i, i.replace(" ","_"))