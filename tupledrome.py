tupl = (1,2,3,3,2,1)
print(tupl)
reverse = tupl[::-1]
print(reverse)

if tupl == reverse:
    print("Its a palindrome")
else:
    print("Its not a palndrome")