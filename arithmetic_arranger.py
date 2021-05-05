def arithmetic_arranger(problems, solution=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  top = []
  bottom = []
  bar = []
  answer = []

  for problem in problems:
    num1, operator, num2 = problem.split()
    if operator not in ("+", "-"):
      return "Error: Operator must be '+' or '-'."
    if not (num1.isnumeric() and num2.isnumeric()):
      return "Error: Numbers must only contain digits."
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

    length = max(len(num1), len(num2)) + 2

    top.extend([" " * (length - len(num1)), num1, " " * 4])
    bottom.extend([operator, " " * (length - len(num2) - 1), num2, " " * 4])
    bar.extend(["-" * length, " " * 4])

    if operator == "+":
      result = int(num1) + int(num2)
    elif operator == "-":
      result = int(num1) - int(num2)
    answer.extend([" " * (length - len(str(result))), str(result), " " * 4])


  if solution:
    return "".join(top)[:-4] + "\n" + "".join(bottom)[:-4] + "\n" + "".join(bar)[:-4] + "\n" + "".join(answer)[:-4]
    
  return "".join(top)[:-4] + "\n" + "".join(bottom)[:-4] + "\n" + "".join(bar)[:-4]