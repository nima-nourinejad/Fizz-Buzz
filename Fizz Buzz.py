def fb (a):
  for i in range (a):
    if (i+1)%3==0 and (i+1)%5==0:
      print ('FB')
    elif (i+1)%3==0:
      print ('F')
    elif (i+1)%5==0:
      print ('B')
    else:
      print (i+1)
