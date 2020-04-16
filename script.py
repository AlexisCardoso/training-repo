#!/bin/python
fname = raw_input("What is your name: ")
print("Hi " + fname)


a = 1
if fname=="Alexis":
  fpass = raw_input("What is your password: ")
  if fpass=="Passw0rd":
    print("You may enter")
  else:
    print("Login failed")
else:
  print("You are not allowed!")
