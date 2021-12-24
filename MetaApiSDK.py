from metaapi_cloud_sdk import MetaStats, MetaApi
import asyncio
import os
from dotenv import load_dotenv
import json

load_dotenv()

async def example():
    # your MetaApi API token
    token = os.getenv('API_TOKEN') or '<put in your token here>'
    # your MetaApi account id
    account_id = os.getenv('ACCOUNT_ID') or '<put in your account id here>'
    # your MetaApi account
    account = None

    api = MetaApi(token)
    meta_stats = MetaStats(token)
    # you can configure http client via second parameter,
    # see in-code documentation for full definition of possible configuration options

    async def account_deploy():
        try:
            nonlocal account
            account = await api.metatrader_account_api.get_account(account_id)

            #  wait until account is deployed and connected to broker
            print('Deploying account')
            if account.state != 'DEPLOYED':
                await account.deploy()
            else:
                print('Account already deployed')
            print('Waiting for API server to connect to broker (may take couple of minutes)')
            if account.connection_status != 'CONNECTED':
                await account.wait_connected()

        except Exception as err:
            print(meta_stats.format_error(err))

    await account_deploy()
    
    async def get_account_metrics():
        try:
            metrics = await meta_stats.get_metrics(account_id)
            print(metrics)  # -> {'trades': ..., 'balance': ..., ...}
        except Exception as err:
            print(meta_stats.format_error(err))

    await get_account_metrics()
    
    async def get_account_open_trades():
        try:
            trades = await meta_stats.get_account_open_trades(account_id)
            print(json.dumps(trades, indent=2))  # -> {_id: ..., gain: ..., ...}
        except Exception as err:
            print(meta_stats.format_error(err))

    await get_account_open_trades()

asyncio.run(example())