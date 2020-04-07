
def day_interval(tk, tc):
    '''Takes two string representing two dates(started cheating time - 'tc' 
    and the got killed time - 'tk'),
    Return a numeric number for days between these two days'''

    from datetime import datetime
    
    a = datetime.strptime(tk[:(len(tk) - 4)] , '%Y-%m-%d %H:%M:%S')
    b = datetime.strptime(tc, '%Y-%m-%d')
    interval = b - a
    return interval.days