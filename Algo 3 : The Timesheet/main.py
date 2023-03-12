from datetime import datetime, timedelta
import time
parent_list = open('TT_small.txt', 'r').read().split('\n')
parent_list.pop(0)
# spilt the list to access elements

# split inner list
for i in range(len(parent_list)):
    parent_list[i] = parent_list[i].split('  ')

parent_list.sort()
# adding missing clk-out timings
for i in range(len(parent_list)):
    if parent_list[i][2] == 'clock-in' and parent_list[i+3][2] != 'clock-out':
        dtm = datetime.strptime(parent_list[i][1], '%Y-%m-%d %H:%M:%S')
        if dtm.hour + 6 < 20 and dtm.minute < 31:
            t = datetime.strptime(
                parent_list[i][1], '%Y-%m-%d %H:%M:%S')+timedelta(hours=6)
            parent_list.append(
                [parent_list[i][0], t.strftime('%Y-%m-%d %H:%M:%S'), 'clock-out'])
        else:
            t = datetime.strptime(
                parent_list[i][1], '%Y-%m-%d %H:%M:%S')+timedelta(seconds=0-dtm.second, minutes=30-dtm.minute, hours=19-dtm.hour)
            parent_list.append(
                [parent_list[i][0], t.strftime('%Y-%m-%d %H:%M:%S'), 'clock-out'])


parent_list.sort()
for i in range(len(parent_list)):
    temp = parent_list[i][1]
    parent_list[i][1] = datetime.strptime(
        temp, '%Y-%m-%d %H:%M:%S').timestamp()
i = 4
k = 7
j = 0
n = 6
m = 5
emparr1 = [parent_list[3][1]-parent_list[0][1]]
emparr2 = [parent_list[2][1]-parent_list[1][1]]
while k < len(parent_list):
    if parent_list[k][0] != parent_list[k-4][0]:
        j += 1
        emparr1.append(0)
    emparr1[j] += parent_list[k][1]
    k += 4
j = 0
while i < len(parent_list):
    if parent_list[i][0] != parent_list[i-4][0]:
        j += 1
    emparr1[j] -= parent_list[i][1]
    i += 4
j = 0
while n < len(parent_list):
    if parent_list[n][0] != parent_list[n-4][0]:
        j += 1
        emparr2.append(0)
    emparr2[j] += parent_list[n][1]
    n += 4
j = 0
while m < len(parent_list):
    if parent_list[m][0] != parent_list[m-4][0]:
        j += 1
    emparr2[j] -= parent_list[m][1]
    m += 4
for i in range(len(emparr1)):
    emparr1[i] = emparr1[i] - emparr2[i]


avg = 0
f = open("out.txt", "w")
f.write(time.strftime("%H:%M:%S", time.gmtime(max(emparr1))) +
        " "+time.strftime("%H:%M:%S", time.gmtime(min(emparr1)))+" ")

for i in range(len(emparr1)):
    avg += emparr1[i]
    emparr1[i] = time.strftime("%H:%M:%S", time.gmtime(emparr1[i]))
f.write(str(time.strftime("%H:%M:%S", time.gmtime((avg/len(emparr1))))))
f.close()
print('Successful!')
