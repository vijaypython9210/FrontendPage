user_input=input('Enter Palidrome Number/Words')
rev_user_input=(str(user_input))[::-1]
if user_input==rev_user_input:
    print('true')
else:
    print('false')