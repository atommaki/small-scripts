#!/usr/bin/python3

import configparser
import glob
import base64
import os
import argparse
from Crypto.Cipher import DES3

# Arguments {{{
#parser = argparse.ArgumentParser()
#parser.add_argument(
#    'user@server',
#    help = "user and/or servername in format of 'user@server', 'user' or '@server'",
#    action = "store", dest = "user_and_server")
#args = parser.parse_args()
#print(args.user@server)
# }}} Arguments

config = configparser.ConfigParser()
config.read('/home/robert.kulyassa/.remmina/remmina.pref')
if 'remmina_pref' in config.sections() and 'secret' in config['remmina_pref'].keys():
    secret = base64.b64decode(config['remmina_pref']['secret'])
else:
    raise EnvironmentError("Wrong remmina.pref.") # TODO: exception type


for filename in glob.glob("/home/robert.kulyassa/.remmina/*.remmina"):
    config.read(filename)
    encryptedpassword = base64.b64decode(config['remmina']['password'])
    password = DES3.new(secret[:24], DES3.MODE_CBC, secret[24:]).decrypt(encryptedpassword).decode("utf-8")
    print(f"{config['remmina']['username']}@{config['remmina']['server']}      {password}")

