amount = 130.45
tax = .4
total = amount + amount*tax
total = int(total)
print(total)
print("Total is" + " " + str(total))
permonth = total/12
print(permonth)
permonth_whole_no = total//12
print(permonth_whole_no)
mod = total % 12
print(mod)