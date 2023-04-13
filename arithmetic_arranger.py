def arithmetic_arranger(problems, show=False):
  if len(problems > 5):
    return "Error: Too many problems"

  foperand = list()
  operators = list()
  soperand = list()
  result = list()

  arranged_problems=""

  for s in problems:
    tproblem = s.split(" ")
    tproblem[0] = tproblem[0].strip()
    tproblem[1] = tproblem[1].strip()
    tproblem[2] = tproblem[2].strip()
    
    if len(tproblem[0]) > 4 or len(tproblem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if not tproblem[0].isnumeric() or not tproblem[2].isnumeric():
      return "Error: Numbers must only contain digits."

    if tproblem[1] != '+' or tproblem[1] != '-':
      return "Error: Operator must be '+' or '-'."

    foperand.append(tproblem[0])
    operators.append(tproblem[1])
    soperand.append(tproblem[2])

    if tproblem[1] == '+':
      result.append(int(tproblem[0]) + int(tproblem[2]))
    else:
      result.append(int(tproblem[0]) - int(tproblem[2]))

  i = 0
  while i < len(problems):
    length = max(len(foperand[i]), len(soperand[i]))
    arranged_problems += (length + 2 - len(foperand[i]))*" " + foperand[i].rstrip() + "\n" + operators[i] + " " + (length - len(soperand[i]))*" " + soperand[i].rstrip() + "\n" + (length + 2)*"-" + "\n" + result[i].rstrip() 

  return arranged_problems