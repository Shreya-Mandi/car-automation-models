d1 = eval(input("Enter the values for d1(x,y,ap,acc:"))
d2 = eval(input("Enter the values for d2(x,y,ap,acc:"))
# obj=(x,y,sp,acc)
# y=0 left, y=1 right
# x=0,100


# 0 is cannot, 1 is can
d1_can_acc=0
d1_can_dec=0
d1_can_switch=0


if(d1[3]==0 and d2[3]==0): #uniform motion
  if(d1[1]==d2[1]): # same lane
    if(d1[0]>d2[0]): # d1 in front
      d1_can_acc=1
      d1_can_dec=0
      d1_can_switch=1
    elif (d1[0]<d2[0]): # d1 is behind
      d1_can_acc=0
      d1_can_dec=1
      d1_can_switch=1
  elif(d1[1]!=d2[1]): # different lane
    if(d1[0]==d2[0]): # beside
      d1_can_acc=1
      d1_can_dec=1
      d1_can_switch=0
    elif(d1[0]>d2[0]): # d1 ahead
      d1_can_acc=1
      d1_can_dec=1
      d1_can_switch=0
    elif(d1[0]<d2[0]): # d1 behind
      d1_can_acc=1
      d1_can_dec=1
      d1_can_switch=1
else:
  if(d2[3]>d1[3]): # acc of d2>d1
    if(d1[1]==d2[1]): # same lane
      if(d1[0]>d2[0]): # d1 ahead
        d1_can_acc=1
        d1_can_dec=0
        d1_can_switch=1
      elif (d1[0]<d2[0]): # d1 behind
        d1_can_acc=0
        d1_can_dec=1
        d1_can_switch=1
    elif(d1[1]!=d2[1]): # diff lane
      if(d1[0]==d2[0]): # beside
        d1_can_acc=1
        d1_can_dec=1
        d1_can_switch=0
      elif(d1[0]>d2[0]): # d1 ahead
        d1_can_acc=1
        d1_can_dec=1
        d1_can_switch=0
      elif(d1[0]<d2[0]): # d1 behind
        d1_can_acc=1
        d1_can_dec=1
        d1_can_switch=1
  elif (d2[3]<d1[3]): # acc of d1>d2
    if(d1[1]==d2[1]): # same lane
      if(d1[0]>d2[0]): # d1 ahead
        d1_can_acc=1
        d1_can_dec=0
        d1_can_switch=1
      elif(d1[0]<d2[0]): # d1 behind
        d1_can_acc=0
        d1_can_dec=1
        d1_can_switch=1
    elif(d1[1]!=d2[1]): #diff lane
      if(d1[0]==d2[0]):  #beside
        d1_can_acc=1
        d1_can_dec=1
        d1_can_switch=0
      elif(d1[0]>d2[0]): # d1 ahead
        d1_can_acc=1
        d1_can_dec=1
        d1_can_switch=1
      elif(d1[0]<d2[0]): # d1 behind
        d1_can_acc=1
        d1_can_dec=1
        d1_can_switch=0

print(d1_can_acc,d1_can_dec,d1_can_switch)
