#0. \n : 이스케이프 시퀸스
#1. \n : 엔터키
#2. \t : 탭
#3. \\ : \ """


 #두개의 수를 곱하기

a, b = input( "곱셈할 두 수를 입력하세요. 예) 10 4 \n" ).split() #split : 10 4를 분리할때
print(f"두 수의 곱은 {int(a) * int(b)}입니다." )
print(f"{a} x {b} = {int(a) * int(b)}") 


