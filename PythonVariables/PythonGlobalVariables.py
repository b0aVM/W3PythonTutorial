#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

    #x = 'awesome'

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that func.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
