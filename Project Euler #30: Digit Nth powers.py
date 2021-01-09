def Digit_Nth_Powers(n,lower,upper):
  sumList = 0

  for i in range(lower,upper):
    digits = list(map(int,str(i)))
    tempSum = 0

    for j in digits:
      tempSum += j**n
    
    if i == tempSum:
      sumList += i
        
  return sumList

if __name__ == '__main__':
  n = int(input())
  
  # Lower and upper limit is determined by experiments for faster code execution
  if n == 3:
    lower,upper = [1*(10**2), 1*(10**3)]
  elif n == 4:
    lower,upper = [1*(10**3), 1*(10**4)]  
  elif n == 5:
    lower,upper = [2*(10**3), 2*(10**5)]
  elif n == 6:
    lower,upper = [1*(10**5), 6*(10**5)]
    
  sumList = Digit_Nth_Powers(n,lower,upper)
  print(sumList)
