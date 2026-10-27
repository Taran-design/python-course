import time
import random

quiz_results = {}
for i in range(1, 1001):
    quiz_results[i] = random.randint(0, 100)

result_list = list(quiz_results.items())

def constant_search(student_id):
    return quiz_results.get(student_id)

def linear_search(student_id):
    for student, score in result_list:
        if student == student_id:
            return score
        return None
    
def quadratic_search(student_id):
    for student, score in result_list:
        for other_student, other_score in result_list:
            if student == student_id and student == other_student:
                return other_score
        return None

student_id = 750


start = time.perf_counter()
result = constant_search(student_id)
end = time.perf_counter()

print("0(1) Constant search")
print("Score:", result)
print("Time:", end - start)

start = time.perf_counter()
result = linear_search(student_id)
end = time.perf_counter()

print("\n0(n) Linear search")
print("Score:", result)
print("Time:", end - start)

start = time.perf_counter()
result = quadratic_search(student_id)
end = time.perf_counter()

print("\n0(n^2) Quadratic search")
print("Score:", result)
print("Time:", end - start)
