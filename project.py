email=input("Enter Your Email: ").strip()
#email slicer
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
#domain
#username
print(f"Your username is {username} & domain is {domain}")
