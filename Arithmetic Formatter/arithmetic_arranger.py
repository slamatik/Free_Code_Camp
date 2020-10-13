def arithmetic_arranger(problems, display_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    temp_first_line = []
    temp_second_line = []
    temp_dashed_line = []
    temp_answer_line = []

    for question in problems:
        left = question.split()[0]
        operator = question.split()[1]
        right = question.split()[2]

        # Checks
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            if operator == "+":
                answer = int(left) + int(right)
            elif operator == "-":
                answer = int(left) - int(right)
            answer = str(answer)
        except ValueError:
            return "Error: Numbers must only contain digits."

        question_len = max(len(left), len(right)) + 2
        temp_first_line.append(" " * (question_len - len(left)) + left)
        temp_second_line.append(operator + " " * (question_len - 1 - len(right)) + right)
        temp_dashed_line.append("-" * question_len)
        temp_answer_line.append(" " * (question_len - len(answer)) + answer)

    first_line = "    ".join(temp_first_line)
    second_line = "    ".join(temp_second_line)
    dash_line = "    ".join(temp_dashed_line)
    answer = "    ".join(temp_answer_line)
    if display_answer:
        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}\n{answer}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}"
    return arranged_problems


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
