# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
student_scores = [11, 34, 44, 0, 4, 8]
student_scores = sorted(student_scores)

highest = student_scores[0]
    
for i in student_scores:
    if i>highest:
        highest = i
print(f"The highest score in the class is: {highest}")
