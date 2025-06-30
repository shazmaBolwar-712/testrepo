n=int(input('enter n'))
if n<1000:
 discount=0
elif n>1000:
 discount=10/100*n
elif n>5000:
 discount=20/100*n
else:
 discount=25/100*n
print(discount)
final=n-discount
print(final)
