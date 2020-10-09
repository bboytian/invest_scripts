# -------
# imports

import requests

from .bottoken import *


# ------
# params


# -------------
# main function

def func(bot_message):
    '''
    bot_message:: str, message you want to send to the bot
    return:: log reponse as to whether the message sent out succesfully
    '''

    send_text = 'https://api.telegram.org/bot'\
        + bot_token\
        + '/sendMessage?chat_id='\
        + developer_chatID\
        + '&parse_mode=HTML='\
        + bot_message
        # + '&parse_mode=Markdown&text='\
    response = requests.get(send_text)

    return response.json()


msg = \
'''
<pre>\
| Tables   |      Are      |  Cool |\
|----------|:-------------:|------:|\
| col 1 is |  left-aligned | $1600 |\
| col 2 is |    centered   |   $12 |\
| col 3 is | right-aligned |    $1 |\
</pre>\
'''
#     '''
# hello,
# | Tables   |      Are      |  Cool |\n
# |----------|:-------------:|------:|\n
# | col 1 is |  left-aligned | $1600 |\n
# | col 2 is |    centered   |   $12 |\n
# | col 3 is | right-aligned |    $1 |\n
# '''


print(func(msg))

# msg = \
# '<pre>hello</pre>'

# # '\
# # <pre>\
# # | Tables   |      Are      |  Cool |\
# # |----------|:-------------:|------:|\
# # | col 1 is |  left-aligned | $1600 |\
# # | col 2 is |    centered   |   $12 |\
# # | col 3 is | right-aligned |    $1 |\
# # </pre>\
# # '

# print(func(msg))
