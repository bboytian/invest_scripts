# -------
# imports

import bs4
import os.path as osp

import requests
import selenium.webdriver as snwd


# ------
# params

url_dict = {'summary':'https://sg.finance.yahoo.com/quote/{}.SI?p={}.SI&.tsrc=fin-srch'
            , 'statistics':'https://sg.finance.yahoo.com/quote/{}.SI/key-statistics?p={}.SI'
}

#api_dict = {'Price':['summary', 'td', 'data-test', 'PREV_CLOSE-value'],
#}
api_dict = {'Price':['statistics', 'span', 'class', 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']
            # , 'Trailing P/E':['statistics', '']
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
# main func

main_dir = osp.dirname(osp.dirname(osp.dirname(osp.abspath(__file__))))
webdriver_str = 'chromedriver'
os_str = 'linux64'            # available options 'mac64', 'linux64'
ver_str = '79'   # only available option thus far: 79.0.39.45.36
webdriver_str = '{}_{}_{}'.format(webdriver_str, os_str, ver_str)

driver_dir = main_dir + '/_webdriver/' + webdriver_str
chrome_options = snwd.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


stockcode_str = 'O39'
url = url_dict['statistics'].format(stockcode_str, stockcode_str)
driver = snwd.Chrome(driver_dir, options=chrome_options)
driver.get(url)
html_str = driver.page_source

soup = bs4.BeautifulSoup(html_str, 'html.parser')
data = soup.find(string='Trailing P/E').parent.parent.next_sibling.text
print(data)

try: 
    if data:
        msg = \
            '''
            hello
            '''
        raise DeprecationWarning(msg)
except DeprecationWarning:

    print(osp.basename(__file__))


