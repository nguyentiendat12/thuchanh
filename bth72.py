k=open('D:/a.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=l
        if (line[k]==' '):
            wc+=l
        if(line[k]=='\n'):
            wc,lc=wc+1,lc+1
print("the no.of chars is %d\n the no.of words is %d\n the no.of lines is %d"%(char,wc,lc))       
