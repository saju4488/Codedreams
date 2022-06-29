

from regex import P


art_100 = """
YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE      SSSSSSSSSSS
YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE     SSSSSSSSSSSSS
YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE    SSSSSSSSSSSSSSS
YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE    SSSSSSSS    SSS
 YYYYYYYY      YYYYYYYY     EEEEEEEE              SSSSSSSS
  YYYYYYYY    YYYYYYYY      EEEEEEEE              SSSSSSSS
   YYYYYYYY  YYYYYYYY       EEEEEEEEEEEEE          SSSSSSSS
    YYYYYYYYYYYYYYYY        EEEEEEEEEEEEE           SSSSSSSSSS
     YYYYYYYYYYYYYY         EEEEEEEEEEEEE            SSSSSSSSSS
      YYYYYYYYYYYY          EEEEEEEEEEEEE               SSSSSSSSS
       YYYYYYYYYY           EEEEEEEE                     SSSSSSSS
        YYYYYYYY            EEEEEEEE                     SSSSSSSS
        YYYYYYYY            EEEEEEEEEEEEEEEEE     SSS    SSSSSSSS
        YYYYYYYY            EEEEEEEEEEEEEEEEE     SSSSSSSSSSSSSSS
        YYYYYYYY            EEEEEEEEEEEEEEEEE      SSSSSSSSSSSSS
        YYYYYYYY            EEEEEEEEEEEEEEEEE       SSSSSSSSSSS
"""


print(art_100)
print(" !! 100세 시대 !! ")
print(" 나는 어떤 모습일까요?")
print()

age = int(input("현재 나이를 입력해 주세요 >>>>>  "))
rest_of_life = 100 - age
print("여기까지 달려왔어요")
print("*" * age, end = '')
print("_" * rest_of_life)
print()

print("세상은 넓고, 우리에겐 수많은 기회와 새로운 도전들이 기다리고 있습니다.")
print("보다 지헤롭고 보다 풍부한 경험을 지닌 100세의 나 자신을 위해 한 걸음씩 내디뎌 보세요.")
print()
print("지금부터")
print("="*70)
print(f"일년에 한번씩 새로운 취미 만들기에 도전한다면 {rest_of_life}개의 새로운 도전이 기다리고 있어요")
print(f"한달에 한번씩 여행을 간다면 {rest_of_life * 12:,}곳에서 추억을 쌓을 수 있어요")
print(f"일주일에 책 한권씩 읽는다면 {rest_of_life * 52:,}권의 지혜를 얻게 되실거예요")
print(f"하루에 1개의 영어 단어를 외운다면 {rest_of_life * 365:,}개의 영어 단어를 익히게 되실거예요")
print(f"일반 원어민의 어휘력은 약20.000단어입니다")
print("=" *70)
print("계획을 세우고 그 꿈을 위해 한걸음 한걸음씩 내디뎌 보세요")
print()
