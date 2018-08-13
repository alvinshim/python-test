# # 과제 1. 맛집 고르기
#
# # 한식, 중식, 일식 음식점을 각각 리스트로 만든다
# # 사용자가 하나를 고를 수 있도록 입력 장치 구현
# # 사용자 선택에 따라 해당 리스트에서 랜덤으로 하나 추출
# # 결과 출력
#
# kor_res = ["봉추찜닭", "집으로삼겹", "서울도시락", "혼밥대장", "놀부보쌈"]
# chn_res = ["흑룡강", "향도장", "중화각", "양자강", "자금성"]
# jap_res = ["스시안", "김태완스시", "미스터카츠", "바론참치", "길초밥"]
#
# import random
# def int_res(food):
#     if food == "한식":
#         return random.sample(kor_res, 1)
#     elif food == "중식":
#         return random.sample(chn_res, 1)
#     else:
#         return random.sample(jap_res, 1)
#
# food = input("한식, 중식, 일식 중에서 원하는 음식을 입력해주세요: ")
# print(int_res(food))

# # 과제 2. 조직도 만들기
# class Person:
#     def __init__(self, name, age, sex, position):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.position = position
#
# class Coworker(Person):
#     position = "대리"
#
# a = Person('심규일', 30, '남', '매니저')
# print(a.position)


# 과제 3. 가위, 바위, 보 게임

# 사용자 입력
# 컴퓨터 랜덤 선택
# 3번을 지거나, 3번을 이기면 게임 종료
# 결과 비교
# 최종 스코어 (포매팅)

# selection = ['가위', '바위', '보']
# user = input("가위, 바위, 보 중에서 하나를 고르세요. ")
#
# import random
# computer = random.choice(selection, 1)


# 과제 4. 2! 다이아몬드 그리기
