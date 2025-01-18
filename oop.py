# simple sign up and sign in
print('Create Your Account')
userName = input('Create usernName -> ')
passWord = input('Enter the passWord -> ')
print('Sign Up completed....')

log_in = input('Enter Your userName -> ')
log_in_pass = input('Enter Your passWord -> ')

if log_in == userName and log_in_pass == passWord:
    print('User Logged In Successfully...')
else:
    print('Enter right Credientials...')