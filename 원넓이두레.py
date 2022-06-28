
 # 원의 넓이 : 반지름*반지름*3.14
 # 원의 둘레 : 2 * 반자름 * 3.14

 # int : 정수
 # flot : 실수


r = float(input("반지름을 입력해 주세요. \n"))
print(r)

area = r**2 *3.14
circumference = 2*r*3.14

print(f"원의 넓이 : {r*r*3.14}")
#거듭제곱 **   예) 10^2 = 10**2   3^7 = 3**7  r^2 = r ** 2

print(f"원의 넓이(거듭제곱 **) : {round(area, 2)}")  #round는 소수점 2자리까지만 출력
print(f"원의 둘레 : {round(circumference)}")


