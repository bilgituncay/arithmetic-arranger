import operator
def arithmetic_arranger(problems, results = False):

  if len(problems) > 5:
    return 'Error: Too many problems.'
  ops = {
    '+': operator.add,
    '-': operator.sub
  }

  arranged_problems = []
  first_line=[]
  second_line=[]
  third_line=[]
  fourth_line=[]

  for problem in problems:
    parts = problem.split()
    num_length = len(max(parts, key=len))
    if not all([i.isnumeric() for i in parts[::2]]):
      return 'Error: Numbers must only contain digits.'
    elif parts[1] not in ['-', '+']:
      return "Error: Operator must be '+' or '-'."
    elif num_length > 4:
      return "Error: Numbers cannot be more than four digits."

    line_length = num_length + 2
    line = '-' * line_length
    first_num = parts[0].rjust(line_length)
    second_num = f"{parts[1]}{' ' * (line_length - len(parts[2]) - 1)}{parts[2]}"

    if results:
      res = str(ops[parts[1]](int(parts[0]), int(parts[2])))
      fourth_line.append(f"{res.rjust(line_length, ' ')}")

    first_line.append(first_num)
    second_line.append(second_num)
    third_line.append(line)

  arranged_problems = '\n'.join(['    '.join(i) for i in (first_line, second_line, third_line)])
  if results:
    arranged_problems += '\n' + '    '.join(fourth_line)

  return arranged_problems