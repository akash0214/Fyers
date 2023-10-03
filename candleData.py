from fyers_apiv3 import fyersModel
import json

#Extracting token
tokenFile = open('./access_token.json')
tokenObject = json.load(tokenFile)
access_token = tokenObject["access_token"]

#Extracting the credentials
apiCredFile = open('./apiCred.json')
credObject = json.load(apiCredFile)
client_id = credObject["client_id"]

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")
data = {
    "symbol":"NSE:SBIN-EQ",
    "resolution":"15",
    "date_format":"1",
    "range_from":"2023-10-03",
    "range_to":"2023-10-03",
    "cont_flag":"1"
}
data = fyers.history(data=data)
print(data['candles'])