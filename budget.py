class Category:
  name = ""

  def __init__(self, name):
    self.name = name
    self.balance = 0.0
    self.ledger = list()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += float(amount)

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == False:
      return False

    self.ledger.append({"amount": -amount, "description": description})
    self.balance -= float(amount)
    return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount) == False:
      return False

    self.withdraw(amount, "Transfer to " + category.name)
    category.deposit(amount, "Transfer from " + self.name)
    return True

  def check_funds(self, amount):
    if self.balance < amount:
      return False
    return True

  def __str__(self):
    printer = ""
    fline = self.name
    fline = fline.center(30, "*").rstrip()
    printer += fline + '\n'
    for items in self.ledger:
      line = list(items.values())
      right = line[0]
      right = str('%.2f' % right)
      left = line[1]
      left = left[:23].ljust(23)
      right = right[:7].rjust(7)
      printer += left + right + "\n"
    printer += "Total: " + str('%.2f' % self.balance)
    return printer


def create_spend_chart(categories):
  name = list()
  name_length = list()
  cat_items = list()
  withrawals = list()
  percentages = list()
  longest = 0

  bar_chart = "Percentage spent by category\n".rstrip()
  bar_chart += '\n'
  for category in categories:
    name.append(category.name)
    name_length.append(len(category.name))
    if len(category.name) > longest:
      longest = len(category.name)
    subtotal = 0
    for ledger in category.ledger:
      op = list(ledger.values())
      if op[0] < 0:
        subtotal += (-op[0])

    withrawals.append(subtotal)

  total = sum(withrawals)
  for withrawal in withrawals:
    percentages.append(round(withrawal / total, 2) * 100)

  p = 100
  while p >= 0:
    bar_chart += str(p).rjust(3) + "| "
    for per in percentages:
      if per >= p:
        bar_chart += 'o' + 2 * ' '
      else:
        bar_chart += 3 * ' '
    bar_chart += "\n"
    p -= 10

  bar_chart += 4 * " " + (len(percentages) * 3 + 1) * "-"
  bar_chart = bar_chart.rstrip()

  for i in range(longest):
    bar_chart += '\n'
    bar_chart += 5 * " "
    for n in name:
      if i < len(n):
        bar_chart += n[i] + "  "
      else:
        bar_chart += 3 * " "

  print(bar_chart)
  return bar_chart
