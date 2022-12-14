zero,one,two,three,four,five,six,seven,eight,nine,m,a,p,sep,form = [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],[[0,0,1,0,0],[0,1,1,0,0],[1,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]],[[0,1,1,1,0],[1,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1]],[[1,1,1,1,0],[0,0,0,0,1],[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,0]],[[1,0,0,0,0],[1,0,0,0,0],[1,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],[[1,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]],[[0,1,1,1,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,1],[0,1,1,1,0]],[[1,1,1,1,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]],[[0,1,1,1,0],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],[[0,1,1,1,0],[1,0,0,0,1],[0,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,1,1,1,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]],[[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,0,1,0],[1,1,1,1,0],[1,0,0,1,0]],[[0,0,0,0,0],[1,1,1,1,0],[1,0,0,1,0],[1,1,1,1,0],[1,0,0,0,0],[1,0,0,0,0]],[[0,0,0,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,0,0,0],[0,0,2,0,0],[0,0,2,0,0]],'%Y-%m-%d %H:%M %p'
digdict_ = {str(i):v for i,v in enumerate([zero,one,two,three,four,five,six,seven,eight,nine])}
alpdict_ = {'a':a,'m':m,'p':p,':':sep}
all_dict = {**digdict_,**alpdict_}
now = __import__('datetime').datetime.now()
from time import strftime
print(f"Today is {now.year}-{now.month}-{now.day} \n")
lh = ((int(strftime('%H'))+24))%24
h,m= '00'+str(lh), '00'+strftime('%M')
ftime = f"{int(h[-2])}{int(h[-1])}:{int(m[-2])}{int(m[-1])}"
hours,mins = str(int(now.hour)-4), str(now.minute)
meridiem = now.strptime(f'{hours}','%H').strftime('%I %p').split(' ')
full_time = f'{ftime}{meridiem[1].lower()}'
for i in range(6):
    for time in full_time:
        for col in all_dict[time][i]:
           if col == 0:
             print(' ', end = "")
           elif col == 1:
             print('#', end = "")
           elif col == 2:
             print('*', end='')
        print(" ",end="")
    print()
#print(det('st')) if int(now.month) == 1 or str(int(now.month))[-1] == '1' else print(det('nd')) if int(now.month) == 2 or str(now.month)[-1] == '2' else print(det('rd')) if int(now.month) == 3 or str(now.month)[-1] == '3' else print(det('th'))
print()