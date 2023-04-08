from os import environ as env
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEYVAULT_NAME = env.get("key_vault_name", "")
KEYVAULT_SECRET_1 = env.get("secret_name_1")

KEYVAULT_URI = f"https://{KEYVAULT_NAME}.vault.azure.net/"

_credential = DefaultAzureCredential()
_serviceClient = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)

GSPREAD_API_KEY = _serviceClient.get_secret(KEYVAULT_SECRET_1).value