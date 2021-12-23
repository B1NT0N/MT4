import os
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('API_TOKEN')
account_id = os.getenv('ACCOUNT_ID')
server_url = 'https://mt-client-api-v1.agiliumtrade.agiliumtrade.ai'

## Methods
###Returns account information for a specified MetaTrader account
def get_account_info(api_token,account_id,):
    
    headers={'auth-token':api_token}
    account_info = requests.get(f"{server_url}/users/current/accounts/{account_id}/accountInformation?{api_token}",headers=headers)
    
    return account_info.json()

##Returns account information for a specified MetaTrader account
def get_positions_info(api_token,account_id,):
    
    headers={'auth-token':api_token}
    positions_info = requests.get(f"{server_url}/users/current/accounts/{account_id}/positions?{api_token}",headers=headers)
    
    return positions_info.json()

# positions_info=get_account_info(api_token,account_id)
# print(json.dumps(positions_info.json(),indent=2))
