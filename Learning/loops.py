# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# #We could use sum() or len() , but it would be to easy
#
# count = 0
# sum_of_heights = 0
# for i in student_heights:
#     count += 1
#     sum_of_heights += int(i)
#
# print(f"Count: {count}")
# print(f"Sum: {sum_of_heights}")
# average = int(sum_of_heights / count)
# print(f"Average: {average}")

# 78 65 89 86 55 91 64 89

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# high_score = 0
# for highest in student_scores:
#     if high_score < highest:
#         high_score = highest
#
# print(high_score)
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print(total)

#or

total = 0
for i in range(2, 101, 2):
    total += i

print(total)
