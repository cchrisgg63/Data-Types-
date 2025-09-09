
import time

time_wait = 1
wait_time = time_wait * 3   # total wait time
print(f'Project starting in {wait_time} seconds.. ')
time.sleep(wait_time)


#datatypes
list3 = list(('hello', 1, 'you', 6.3, 'yes', 7, 2.3))
print(list3)
for i in range(len(list3)):
  if str(type(list3[i])) == "<class 'str'>":
    list3[i]=list3[i] + ' of course'
  #printing out str class as list with of course attached to each STR

print('list3=', list3)

#if item in list is a float add 5
if str(type(list3[i])) == "<class 'float'>":
  list3[i]=list3[i] + 5


print('list3=',list3)

