# -*- coding: utf-8 -*-
"""
Connecting to KiteConnect API

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

# gen totp

from pyotp import TOTP
TOTP('FVTBQWN7SOK7ZQ43YLWNUKN4QTEX27I7').now()


from kiteconnect import KiteConnect
import pandas as pd

api_key = "njgk5k0sme83h3hn"
api_secret = "hefr3nvtupbgvu4gpp6q6c8iqk8ucjl6"
kite = KiteConnect(api_key=api_key)
print(kite.login_url()) #use this url to manually login and authorize yourself

#generate trading session
request_token = "w45B27hEPhoxwniUdJNDB632wNp2Dcvn" #Extract request token from the redirect url obtained after you authorize yourself by loggin in
data = kite.generate_session(request_token, api_secret=api_secret)

#create kite trading object
kite.set_access_token(data["access_token"])
with open('access_token.txt', 'w') as file:
        file.write(data["access_token"])


#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)
instrument_df.to_csv("NSE_Instruments.csv",index=False)