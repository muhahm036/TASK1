stringInput=input("Enter String:")
countDigit=0
countletter=0

for x in stringInput:
    if x >=  'a' and  x <= 'z' or x >=  'A' and  x <= 'Z':
        countletter=countletter+1
    elif x >= '0' and x <= '9':
        countDigit=countDigit+1

print ("letters:",countletter)
print("digits:",countDigit)