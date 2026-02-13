import numpy as np

# Marks of 5 students in 3 subjects
result = np.array([
    [85, 78, 92],
    [88, 76, 81],
    [90, 89, 95],
    [70, 65, 72],
    [60, 75, 68]
])

print("Marks Matrix:\n", result)

total_marks = result.sum(axis=1)
print("Total marks of each student:", total_marks)

avg_subject = result.mean(axis=0)
print("Average marks of each subject:", avg_subject)

top_student = np.argmax(total_marks)
low_student = np.argmin(total_marks)

print("Top student index:", top_student)
print("Lowest student index:", low_student)

result_with_grace = result + 5

final_result = np.clip(result_with_grace, 0, 100)

print("Final result after grace marks:\n", final_result)
import numpy as np

# Marks of 5 students in 3 subjects
result = np.array([
    [85, 78, 92],
    [88, 76, 81],
    [90, 89, 95],
    [70, 65, 72],
    [60, 75, 68]
])

print("Marks Matrix:\n", result)

total_marks = result.sum(axis=1)
print("Total marks of each student:", total_marks)

avg_subject = result.mean(axis=0)
print("Average marks of each subject:", avg_subject)

top_student = np.argmax(total_marks)
low_student = np.argmin(total_marks)

print("Top student index:", top_student)
print("Lowest student index:", low_student)

result_with_grace = result + 5

final_result = np.clip(result_with_grace, 0, 100)

print("Final result after grace marks:\n", final_result)
