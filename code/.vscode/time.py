print("Days")
D = int(input())
print("Hours")
H = int(input())
print("Minutes")
M = int(input())
print("Seconds")
S = int(input())
Time = 0
Time += int(D * 86400)
Time += int(H * 3600)
Time += int(M * 60)
Time += int(S)
print("In seconds it is: " + str(Time))