def avg(values):
    return sum(values) / len(values)


def solve(students_data):
    students = dict()
    for student in students_data:
        name, result = student.split()
        result = float(result)
        if name not in students:
            students[name] = []
        students[name].append(result)
    for name, results in students.items():
        format_results = ' '.join(f"{x:.2f}" for x in results)
        avg_result = avg(results)
        print(f"{name} -> {format_results} (avg: {round(avg_result, 3):.2f})")


total_lines = int(input())
input_data = [input() for _ in range(total_lines)]

solve(input_data)
