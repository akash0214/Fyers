from fyers_apiv3 import fyersModel
import json

#loading json
apiCredFile = open("./apiCred.json")
apiCredJson = json.load(apiCredFile)

client_id = apiCredJson["client_id"]
secret_key = apiCredJson["secret_key"]
redirect_uri = apiCredJson["redirect_uri"]

session = fyersModel.SessionModel(
    client_id = client_id,
    secret_key = secret_key,
    redirect_uri = redirect_uri,
    response_type = "code",
    grant_type = "authorization_code"
)
url = session.generate_authcode()
print(url)

auth_code = input("Enter auth code: ")
session.set_token(auth_code)
token_response = session.generate_token()

#Serializing json
token_response_object = json.dumps(token_response, indent=4)

with open('access_token.json', "w") as token:
    token.write(token_response_object)
