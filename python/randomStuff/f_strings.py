n: int = 10000000 # n: float = 1e9 or n: int= 1,000,000,000 or '_' instead of ','
print(f'{n:_}')
print(f'{n:,}')


var: str = 'var'
print(f'{var:>20}:')
print(f'{var:<20}:')
print(f'{var:|^20}')   #can add any char after of before too like in this case

from datetime import datetime

now: datetime = datetime.now()
print(f'{now:%d/%m/%y (%H:%M:%S) }  ')
print(f'{now:%c}')
print(f'{now:%I:%M:%p }') # search datetime specifiers on Google