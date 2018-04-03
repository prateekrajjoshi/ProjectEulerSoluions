num= input().split();
for i in range (0,400): 
  num[i]= int(num[i]); #Takes the whole as input and puts it in an array
prod=1;
ansarr=[];
mularr=[];
for i in range (0, 340): #For top to bottom approach
  prod= num[i]*num[i+20]*num[i+40]*num[i+60];
  ansarr.append(prod);
prod=1;
for i in range (0,400): #For Left to right
  if(((i+1)%20!=0) and ((i+1)+2)%20!=0 and ((i+1)+1)%20!=0):
    prod= num[i]*num[i+1]*num[i+2]*num[i+3];
    ansarr.append(prod);
prod=1;
for i in range (0,400): #For Diagonal:top-left to bottom-right
  if(((i+1)%20!=0) and ((i+1)+2)%20!=0 and ((i+1)+1)%20!=0 and (i+1)<=340):
    prod= num[i]*num[i+21]*num[i+42]*num[i+63];
    ansarr.append(prod);
for i in range (0,400):  #For diagonal:top-right to bottom-left
  if(((i+1-1)%20!=0) and ((i+1)-2)%20!=0 and ((i+1)-31)%20!=0 and (i+1)<=340 and i!=0 and i!=1 and i!=2):
    prod= num[i]*num[i+19]*num[i+38]*num[i+57];
    ansarr.append(prod);

print(max(ansarr));
    