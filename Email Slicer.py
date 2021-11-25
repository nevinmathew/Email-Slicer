email = input("Enter Your Email: ").strip()
userName = email[:email.index('@')]
emailServiceProvider = email[email.index('@') + 1:email.index('.')]
domain = email[email.index('@') + 1:]


#A python program to get an email ID
#as input and slicing it into username,
#email service provider and domain name. 
