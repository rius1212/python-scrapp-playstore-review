from google_play_scraper import Sort, reviews
import xlsxwriter
from json_excel_converter import Converter 
from json_excel_converter.xlsx import Writer


result, continuation_token = reviews(
    'com.bca.smartbranch',
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=2338, # defaults to 100
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'com.bca.smartbranch',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)

conv = Converter()
conv.convert(result, Writer(file='hasil.xlsx'))
