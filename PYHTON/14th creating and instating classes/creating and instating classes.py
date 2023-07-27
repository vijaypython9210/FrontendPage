class employee:
    def init (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + ' . ' + last + '@company.com'
    def fullname(self):
        return self.first + ' ' + self.last
emp_1=employee('john','doe',50000)
print("email:",emp_1.email)
print("pay:",emp_1.pay)
print("fullname:",emp_1.fullname())
emp_2=employee('jane','daf',60000)
print("email:",emp_2.email)
print("pay:",emp_2.pay)
print("fullname:",emp_2.fullname())
emp_3=employee('jack','son',70000)
print("email:",emp_3.email)
print("pay:",emp_3.pay)
print("fullname:",emp_3.fullname())
emp_4=employee('ken','kevin',80000)
print("email:",emp_4.email)
print("pay:",emp_4.pay)
print("fullname:",emp_4.fullname())
