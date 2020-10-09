# -------
# imports

import os.path as osp

import bs4
import requests


# ----------
# API params
'''
Note if the data is 'None' this could be because api_dict is not configured for 'requests', but for 'chromedriver instead'

We have opted for text search for all keywords excluding 'Price'

all information can be taken from the statistics tab
'''

api_dict = {'Price':['summary', 'span', 'class', 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']
            # , 'Trailing P/E':[]
            # , 'Price to Book (mrq)':
            # , 'Profit Margin':
            # , 'Operating Margin (ttm)':
            # , 'Return on Asset':
            # , 'Return on Equity':
            # , 'Diluted EPS (ttm)':
            # , 'Total Debt /Equity (mrq)':
            # , 'Current ratio':
            # , 'Beta':
            # , '52 week high':
            # , '52 week low':
            # , '50 Day Moving Average':
            # , 'Forward Annual  Div Rate':
            # , 'Payout Ratio':
}


# ---------
# relv func

def retr_func(keyword, soup):
    # retreiving data
    try:
        if keyword == 'Price':
            api_lst = api_dict[keyword]
            data = soup.find(api_lst[1], {api_lst[2]:api_lst[3]}).text
        else:
            data = soup.find(string=keyword).parent.parent.next_sibling.text            

    # catching API depreciation, or log
    except AttributeError:
        data = 'MISSING'    # if soup.find[.parent...] is None    

    if not data:
        data = 'MISSING'

    return data

        

    

# ---------
# main func

def func(ex_str, stockcode_str, keyword_lst, *drivers):
    '''
    ex_str:: exchange market, 
    keyword_lst:: labels given in datastore.xlsx
    return:: lst of data, in order of keyword_lst
    '''

    # retriving url
    if ex_str:
        stockcode_str += '.SI'
    stat_url = 'https://sg.finance.yahoo.com/quote/{}/key-statistics?p={}'    
    stat_url = stat_url.format(stockcode_str, stockcode_str)

    sum_url = 'https://sg.finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch'
    sum_url = sum_url.format(stockcode_str, stockcode_str)      
         

    if drivers:                  # using selenium
        stat_driver = drivers[0]
        stat_driver.get(stat_url)
        stathtml_str = stat_driver.page_source
        
        sum_driver = drivers[0]
        sum_driver.get(sum_url)
        sumhtml_str = sum_driver.page_source
        
    else:                       # using requests
        stathtml_str = requests.get(stat_url).content
        sumhtml_str = requests.get(sum_url).content
        
    stat_soup = bs4.BeautifulSoup(stathtml_str, 'html.parser')    
    sum_soup = bs4.BeautifulSoup(sumhtml_str, 'html.parser')    

    ret_lst = []
    keydep_lst = []
    for keyword in keyword_lst:

        data = retr_func(keyword, stat_soup)
        if data == 'MISSING':
            data = retr_func(keyword, sum_soup)
        
        ret_lst.append(data)
        
    return ret_lst

        
        
    
    
