import time

current_time=time.strftime('%H:%M:%S')
print(current_time)
if(current_time>='8:00:00' and current_time<='11:00:00'):
    print("GOOD MORNING SIR!")
elif(current_time>='12:00:00' and current_time<='17:00:00'):
    print("GOOD AFTERNOON SIR!")
elif(current_time>='18:00:00' and current_time<='20:00:00'):
    print("GOOD EVENING SIR!")
elif(current_time>='21:00:00' and current_time<='23:00:00'):
    print("GOOD NIGHT SIR!")