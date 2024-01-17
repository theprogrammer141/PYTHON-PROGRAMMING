#DEFAULT ARGUMENTS
# def average(a=9,b=1):
#     print("average =",(a+b)/2)
#
# average()

#KEYWORD ARGUMENTS
# def name(fname,mname,lname):
#     print("HELLO",fname,mname,lname)
#
# name("PETER","BEN","PARKER")

#REQUIRED ARGUMENTS
# def average(a,b,c=1):
#     print("Average =",(a+b+c)/2)
#
# average(6,7)

#VARIABLE LENGTH ARGUMENTS
# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("AVERAGE =",sum/len(numbers))
#
# average(5,6)
# average(5,6,7,4)