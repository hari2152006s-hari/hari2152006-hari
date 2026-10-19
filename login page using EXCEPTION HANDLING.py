try:
 username=input("enter your name or email:")
 password=int(input("enter your password:"))
except NameError:
    print("enter your name or email idyat")
except ValueError:
    print("please enter numeric value")
finally:
    print("welcome")

