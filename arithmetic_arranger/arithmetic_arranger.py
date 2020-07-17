def arithmetic_arranger(problems, showans=False):
    
    line1, line2, dashes, answers = '', '', '', ''
    numbers2 = []
    operators = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        num1, operator, num2 = problem.split()

        # Testing inputs
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        if num1.isdigit() == False or num2.isdigit() == False:
            return "Error: Numbers must only contain digits."

        if len(num2) > 4 or len(num1) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        line1 = line1 + num1.rjust(width, " ") + "    "
        line2 = line2 + operator + num2.rjust(width - 1, " ") + "    "
        dashes = dashes + '-'*width + "    "
        if showans == True:
            answers = answers + str(eval(num1 + operator + num2)).rjust(width, " ") + "    "
    if showans == True:
        return line1.rstrip() + '\n' + line2.rstrip() + '\n' + dashes.rstrip() + '\n' + answers.rstrip()
    else:
        return line1.rstrip() + '\n' + line2.rstrip() + '\n' + dashes.rstrip()


