def arithmetic_arranger(problems, display_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."



    first_line = ""
    second_line = ""
    dash_line = ""
    answer = ""
    arranged_problems = f"{first_line}\n{second_line}\n{dash_line}\n{answer}"

    return arranged_problems


print(arithmetic_arranger(["32 + 698",
                           "3801 - 2",
                           "45 + 43",
                           "123 + 49"]))
