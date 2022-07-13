
# 숫자 처리 함수
print(abs(-5)) #절대값.
# max , min , round 반올림

from math import *
print(floor(4.19)) # 내림 
print(ceil(3.14)) #올림

#랜덤
from  random import *
print(random())     # 소수점으로 나옴 0.0~1.0 사이의 임의값
print(random()*10)  #0.0 ~10.0

print(int(random()*100)) #0~100 미만의 정수 
print(int(random()*45)+1) #1~45 이하의 정수 

print(randrange(1,46))  #1~45 사이의 값 , 46 미만
print(randint(1, 45))   #1~45 사이의 값 , 45 이하


# slicing
jumin = "112233-1234567"
print("성별 : " + jumin[7]) #8번째가 성별 코드이니까
print("년   : " + jumin[0:2]) # 0 부터 2 직전 까지 
print("월   : " + jumin[2:4]) # 
print("일   : " + jumin[4:6]) # 
print("생년월일 : " + jumin[:6]) # 처음부터 6 앞까지 
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지 
print("뒤 7자리 - 뒤에부터 : " + jumin[-7:])  # 맨뒤 7번째 부터 끝까지 

#문자열 처리 함수 
python = "Python is Amazing"
print(python.lower()) # 소문자로  
print(python.upper())  #대문자로
print(python[0].isupper()) #첫문자가 대문자인지
print(len(python)) #길이
print(python.replace("Python" , "C++")) #대체 - python 원본 자체를 바꾸는건 아님 
print(python) 
index = python.index("n") # n 위치 찾아주기  
print(index) 
index = python.index("n" , index + 1) # 앞에서 찾은 n 다음 부터 다시 n 위치 찾아주기  
print(index) 
print(python.find("n")) # 다른 찾기 함수
print(python.find("C++")) # 다른 찾기 함수 // 못 찾으면 -1 반환
# print(python.index("C++")) # 원하는게 없으면 오류를 발생시키고 끝남.. 고로 find사용하자
print(python.count("n")) # n몇개 있는지 찾기

#문자열 포맷  1:00:59
print("a" + "b")
print("c", "d") #자동으로 공백 추가됨

#method 1
print("Age is %d" %20) 
print("I like %s " % "C++") 
# %s 는 정수 , 문자열 상관없이 사용 가능 
print("Age is %s " %3.14) 
print(" %s %f" % ("문자열과 숫자", 3.14))   # 여러개 조합

#method 2  1:05:00
print("I am {} years old {}" .format(20,"멍청이")) # {} 사이에 .format 있는걸 삽입 
print("I am {1} years old {0}" .format("멍청이",20)) # {} 순서 바꾸기 .. 번호로

#method 3  1:07:00
print("I am {age} years old {string}" .format(string = "멍청이",age=20)) # {} 변수 형식으로 대체하기 

#method 4  1:08:20
age2 = 20 
string2 = "멍청이"
print(f"I am {age2} years old {string2}") # ver 3.6 이상에서 가능 .. 문자열 앞에 f 붙여야 함

# 탈출문자 1:09:20
print("백문이 불여일견 \n백견이 불여일타")  #줄바꿈
print('백문이 "불여일견" 백견이 "불여일타"')  # 따옴표 표시 .. 작은따옴표로 하고 안쪽에서 쌍따옴표 표시로 
print("백문이 \"불여일견\" 백견이 \"불여일타\"")  # 따옴표 표시 
print("탈출문자 역 \\ 표시 ") 
print("경로표시 c:\\work\\  ") 
print("Red Apple \rPine") # 커서 맨앞 이동 해서 다시 출력 ..PineApple 출력
print("한글자 지우기 back\bbac이후 연결") 


# 1:17:20 부터 



