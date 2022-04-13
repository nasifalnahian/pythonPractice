# first_exp = [5,6,7,8,5]
# second_exp = [6,5,4,3,3]
# total = 0
# for item in  first_exp:
#     total = total + item
#
#     print("first_exp total is : ",sum (first_exp))
#     break
# print(first_exp)

# tom_exp_list = [2100,3400,3500]
# joe_exp_list = [200,500,700]

# total=0
# for item in tom_exp_list:
#     total=total+item
#     print("tom's total expense;",total)

def calculate_total(exp):
    total = 0
    for item in exp:
      total = total + item
    return  total
tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]
tom_total= calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)
print("toms total expese:",tom_total)
print("joes total expese:",joes_total)