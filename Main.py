def add_time(start, duration, day=None):
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    start_hour = ''
    start_minute = ''
    meridian = start[-2:]
    duration_hour = ''
    duration_minute = ''
    first = True
    f_first = True
    
    for pos, s in enumerate(start):
        if s != ':':
            if first == True:
                start_hour = start_hour+s
            else:
                if s not in meridian:
                    start_minute = start_minute+s
        else:
            first = False
                
    for pos, s in enumerate(duration):
        if s != ':':
            if f_first == True:
                duration_hour = duration_hour+s
            else:
                duration_minute = duration_minute+s
        else:
            f_first = False
            
           
    
    current_hour = int(start_hour)
    day_count = 0
    duration_hour = int(duration_hour)+(int(duration_minute)//60)
    residual_minute = int(duration_minute)%60
    
    for _ in range(0, (int(duration_hour)+1)):
        if current_hour != 12:
            current_hour += 1
        else:
            if meridian == 'AM':
                current_hour = 0
                current_hour += 1
                meridian = 'PM'
            else:
                current_hour = 0
                current_hour += 1
                meridian = 'AM'
                day_count += 1
                
    if (residual_minute+int(start_minute)) > 60:
        current_minute = (residual_minute+int(start_minute))-60
        if current_hour != 12:
            current_hour += 1
        else:
            if meridian == 'AM':
                current_hour = 0
                current_hour += 1
                meridian = 'PM'
            else:
                current_hour = 0
                current_hour += 1
                meridian = 'AM'
                day_count += 1
    else:
        current_minute = residual_minute+int(start_minute)
       
    if day != None:
        current_day = day
        for t in range(0, (int(day_count))):
            if current_day.lower() == 'sunday':
                current_day = 'Monday'
            elif current_day.lower() == 'monday':
                current_day = 'Tuesday'
            elif current_day.lower() == 'tuesday':
                current_day = 'Wednesday'
            elif current_day.lower() == 'wednesday':
                current_day = 'Thursday'
            elif current_day.lower() == 'thursday':
                current_day = 'Friday'
            elif current_day.lower() == 'friday':
                current_day = 'Saturday'
            elif current_day.lower() == 'saturday':
                current_day = 'Sunday'
    
    if current_hour == 1:
        current_hour = 12
    else:
        current_hour = current_hour-1
        
    if day == None:
        if current_minute < 10:
            if day_count == 0:
                return f'{current_hour}:0{current_minute} {meridian}'
            elif day_count == 1:
                return f'{current_hour}:0{current_minute} {meridian} (next day)'
            else:
                return f'{current_hour}:0{current_minute} {meridian} ({day_count} days later)'
        else:
            if day_count == 0:
                return f'{current_hour}:{current_minute} {meridian}'
            elif day_count == 1:
                return f'{current_hour}:{current_minute} {meridian} (next day)'
            else:
                return f'{current_hour}:{current_minute} {meridian} ({day_count} days later)'
    else:
        if current_minute < 10:
            if day_count == 0:
                return f'{current_hour}:0{current_minute} {meridian}, {current_day}'
            elif day_count == 1:
                return f'{current_hour}:0{current_minute} {meridian}, {current_day} (next day)'
            else:
                return f'{current_hour}:0{current_minute} {meridian}, {current_day} ({day_count} days later)'
        else:
            if day_count == 0:
                return f'{current_hour}:{current_minute} {meridian}, {current_day}'
            elif day_count == 1:
                return f'{current_hour}:{current_minute} {meridian}, {current_day} (next day)'
            else:
                return f'{current_hour}:{current_minute} {meridian}, {current_day} ({day_count} days later)'

