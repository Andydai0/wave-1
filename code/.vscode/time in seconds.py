print("insert number of seconds ")
S = int(input())


Days = S // 86400
S %= 86400
Hours = S // 3600
S %= 3600
Minutes = S // 60
S %= 60
Seconds = S

print(str(Days).zfill(2) + ":" + str(Hours).zfill(2) + ":" + str(Minutes).zfill(2) + ":" + str(Seconds).zfill(2))