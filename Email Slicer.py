email = input("Enter Your Email: ").strip()

userName = email[:email.index('@')]

emailServiceProvider = email[email.index('@') + 1:email.index('.')].capitalize()

domain = email[email.index('@') + 1:]

print("Username: " + userName + "\nEmail Service Provider: " + emailServiceProvider + "\nDomain: " + domain)