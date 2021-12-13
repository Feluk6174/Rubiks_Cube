import test, test2

times_m1 = []
times_m2 = []
for i in range(40):
    print(i)
    times_m1.append(test.timer())

for i in range(40):
    print(i)
    times_m2.append(test2.timer())

total = 0
for time in times_m1:
    total += time

avg_m1 = total/len(times_m1)

total = 0
for time in times_m2:
    total += time

avg_m2 = total/len(times_m1)

print(avg_m1)
print(times_m1)

print(avg_m2)
print(times_m2)