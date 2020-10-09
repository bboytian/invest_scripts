# -------
# imports

import datetime as dt

import telegram as tel

from .._notifier import main as _nf


# ---------
# main func



def func(
        event_str,
        elnid_str, account_str, mature_ts, 
        sreccol_sr, sdatcol_sr,
        kofactor_flt, kifactor_flt, strikefactor_flt
):
    # creating default msg
    msg = \
'''<pre>
ELN id   : {}
Account  : {}
Date     : {:%Y-%m-%d}
Maturity : {:%Y-%m-%d}
Event    : {}
KO Factor: {}
KI Factor: {}
S  Factor: {}

|*|Code | OP    | CP    | %   |
|-|-----|-------|-------|-----|
'''

    format_lst = [
        elnid_str, account_str,
        dt.datetime.now(), mature_ts,
        event_str,
        kofactor_flt, kifactor_flt, strikefactor_flt        
    ]

    if event_str[-1] != '+':    # do not have to buy any stocks
        for code in sreccol_sr.index:

            # handling decimal places            
            srec_flt = sreccol_sr[code]
            if srec_flt >= 100:
                deci_int = 3
                msg += \
                    '|{:1}|{:5}|{:7.3f}|{:7.3f}|{:5.1f}|\n'
            else:
                deci_int = 2
                msg += \
                    '|{:1}|{:5}|{:7.4f}|{:7.4f}|{:5.1f}|\n'

            # getting prices
            op_flt = sreccol_sr[code] # original price
            cp_flt = sdatcol_sr[code] # current price
            per_flt = 100 * cp_flt / op_flt # percentage

            # handling different events
            if event_str in ['Mature', 'KO']:
                format_lst += ['*', code, op_flt, cp_flt, per_flt]

            elif event_str == 'KI':
                if per_flt < kifactor_flt * 100:
                    format_lst += ['*', code, op_flt, cp_flt, per_flt]
                else:
                    format_lst += ['', code, op_flt, cp_flt, per_flt]


    else:                       # may have to buy worst performing stk
        # determine if ELN has recovered
        recovboo_sr = (sdatcol_sr > strikefactor_flt*sreccol_sr)
        recov_boo = recovboo_sr.all()
        per_sr = 100 * sdatcol_sr / sreccol_sr
        worstper_flt = per_sr.min()


        for code in sreccol_sr.index:

            # handling decimal places            
            srec_flt = sreccol_sr[code]
            if srec_flt >= 100:
                deci_int = 3
                msg += \
                    '|{:1}|{:5}|{:7.3f}|{:7.3f}|{:5.1f}|\n'
            else:
                deci_int = 2
                msg += \
                    '|{:1}|{:5}|{:7.4f}|{:7.4f}|{:5.1f}|\n'

            # getting prices
            op_flt = sreccol_sr[code] # original price
            cp_flt = sdatcol_sr[code] # current price
            per_flt = 100 * cp_flt / op_flt # percentage
            
            # handling recovery boolean
            if recov_boo:
                format_lst += ['', code, op_flt, cp_flt, per_flt]
            else:
                if per_flt == worstper_flt:
                    format_lst += ['*', code, op_flt, cp_flt, per_flt]
                else:
                    format_lst += ['', code, op_flt, cp_flt, per_flt]


    # Append rest of message 
    msg += \
        '</pre>'
    msg = msg.format(*format_lst)

    
    # sending message
    _nf('investtianbot', 'html', msg, sendclient_boo=True)
