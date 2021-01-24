# # 계단

# num = int(input())
# for i in range(1, num + 1):
#     for j in range(1, i + 1)
#         print(j, end = ' ')
#     print()


# # 최댓값과 등장횟수
# numbers = [7, 10, 22, 7, 22, 22]

# max_val = numbers[0]
# count = 0

# for val in numbers:
#     if val > max_val:
#         max_val = val
#         count = 1
        
#     elif val == max_val:
#         count += 1

# print(max_val, count)

# # 달팽이
# def snail(height, day, night):
#     # 1. 변수 초기화(걸린 일자)
#     count = 0
    
#     while True:
#         # 1.새로운 아침
#         count += 1
        
#         # 2.달팽이는 뚠뚠 열심히 뚠뚠
#         height -= day
        
#         # 3.기둥에 도착하면 날짜를 반환하고 함수를 끝낸다.
#         if height <=0:
#             return count
        
#         # 4.기둥에 도착 못하면? 밤이 돼서 기둥에서 미끄러진다.
#         height += night



num = int(input())

def sum_of_digit(number):
    if number == 0:
        return number
    mod = number // 10
    remainder = number % 10
    return remainder + sum_of_digit(mod)

print(sum_of_digit(num))
