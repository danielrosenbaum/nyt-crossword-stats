import requests
import pandas as pd
from keys import ACCOUNT_ID    


start_date = '1994-11-21'
end_date = '2023-12-31'

daterange = pd.date_range(start=start_date, end=end_date, freq='100D')

for single_date in daterange:
    current_date = single_date.strftime("%Y-%m-%d")
    query = f'https://www.nytimes.com/svc/crosswords/v3/{ACCOUNT_ID}/puzzles.json?publish_type=daily&date_start={start_date}&date_end={end_date}'
    r = requests.get(url = query)
    data = r.json()
    start_date = current_date






