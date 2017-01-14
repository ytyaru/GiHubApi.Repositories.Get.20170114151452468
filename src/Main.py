#!python3
#encoding:utf-8

import os
from pathlib import Path
from github import Repository
from github import Account

db_path_account = 'C:/GitHub.Accounts.sqlite3'
username = 'github_username'

account = Account.Account(db_path_account)
account.set_username(username)

r = Repository.Repository()
if (account.get_otp() is None):
    r.gets(token=account.get_token())
else:
    r.gets(otp=account.get_otp(), token=account.get_token())
