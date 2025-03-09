student_scores = [150, 155, 80, 90, 199, 160, 189, 110, 100, 85, 81, 98, 96, 156]

# print(max(student_scores))
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score)