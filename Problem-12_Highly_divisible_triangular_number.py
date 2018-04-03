numbs=[];
count=0;
num=0;
for i in range(1, 50000): #Making an array of triangular numbers
  num= num+i;
  numbs.append(num);


for i in range(0, len(numbs)):
  for j in range (1, round(numbs[i]**0.5)): 
    if (numbs[i]%j==0):
      count= count+2; #
  count= count+1; #counting the number itself
  if (count> 500): 
    break;
  count=0;
print(numbs[i]);