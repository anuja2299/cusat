def palindrome(n):
  lenn = len(n)

  j = -1
  for i in range(0,int(lenn/2)):
    if(n[i]==n[j]):
      j= j-1
      fg =1
      continue
    else:
      fg = 0

      break
  if(fg==1):
    print("is a palindrome")
  else:
    print("not a palindrome")
def reverse(n):
  if(n[::-1]==n):
    print("is a palindrome")
  else:
    print("not a palindrome")

string = input("enter the string")
#palindrome(string)
reverse(string)