# -------
# imports

import telegram as tel

from .bottoken import *


# ------
# params

# message formats
parsemode_dic = {
    'html':tel.ParseMode.HTML,
    'markdown':tel.ParseMode.MARKDOWN
}


# ----------------------
# typical message format

# This is the max table length for iPhone 7 screen size
_msg = \
'''
event: KI
<pre>
| Tables   |   Are    |  Cool |
|----------|:--------:|------:|
| col 1 is |  left    | $1600 |
| col 2 is |  cent    |   $12 |
| col 3 is | right    |    $1 |
</pre>
'''

# ---------
# main func

def main(botname, parsemode, msg, sendclient_boo=True):
    '''
    Parameters
        botname (str): name of bot, refer to dict above
        parsemode (str): format of message, refer to dict above
        msg (str): the message
        senddev_boo (boolean): decide whether or not send msg to papa
    '''
    bot = tel.Bot(token=bottoken_dic[botname])

    bot.send_message(
        chat_id=developer_chatID,
        text=msg,
        parse_mode=tel.ParseMode.HTML
    )

    if sendclient_boo:
        bot.send_message(
            chat_id=client_chatID,
            text=msg,
            parse_mode=tel.ParseMode.HTML
        )

# -------
# testing

if __name__ == '__main__':

    msg = \
    '''<pre>
ELN id   :
event    : KI
KO Factor:
KI Factor:
S Factor :

|B|Code | OP    | CP    | %   |
|-|-----|-------|-------|-----|
|{:1}|{:5}|{:6.4f}|{:6.4f}|{:4.1f}|

B : Bought
OP: Original Price
CP: Closing  Price
    </pre>
    '''.format(
        '', 'RDS', 25.97488, 25.974,  100,

    )

    main('investtianbot', 'html', msg, sendclient_boo=False)
