def highpayment(high):
  total=high*(1+0.01*20)
  print(total)
def lowpayment(low):
  total=low*(1+0.01*20)
  print(total)
a=int(input("Enter Salary: "))
if a>=1000000:
  highpayment(a)
elif a>=500000:
  lowpayment(a)
else:
  print("bonus not applied")

 