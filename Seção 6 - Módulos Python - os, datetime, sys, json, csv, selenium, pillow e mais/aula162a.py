from datetime import datetime
from pytz import timezone


data = datetime.now()
print('hora atual:', data)

data = datetime.now(timezone('Asia/Tokyo'))
print('hora atual em Tokyo:', data)

print('número em segundos desde 1970:', data.timestamp())
print('data criada usando timestamp:', datetime.fromtimestamp(1782898304))
