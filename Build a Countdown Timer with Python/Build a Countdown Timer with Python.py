import time

timer = int(input('Enter time in seconds:'))

while timer >= 0 :
    time.sleep(1)
    hour = timer // 60
    minutes = timer % 60
    formatted_time = f'{hour:02d}:{minutes:02d}'
    print(formatted_time)
    timer -= 1
    
    

print('Time\'s up')