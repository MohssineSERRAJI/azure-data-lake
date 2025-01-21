# https://learn.microsoft.com/en-us/azure/databricks/dbfs/mounts
# Configuration pour l'authentification Azure
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    # Identifiant unique de l'application dans Azure Active Directory
    # Obtenu lors de l'enregistrement de l'application dans Azure AD
    "fs.azure.account.oauth2.client.id": "<application-id>",
    # Clé secrète pour l'authentification
    # À stocker de préférence dans un coffre-fort de secrets (Key Vault)
    "fs.azure.account.oauth2.client.secret": "<service-credential-key-name>",
    # URL du service d'authentification Azure AD
    # Contient l'ID du locataire (tenant) Azure AD
    "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<active-directory-id>/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}



# Tester la validité des identifiants
# Construction de l'URL du conteneur Azure
storage_account = "<storage-account-name>"
container = "<container-name>"
url = f"abfss://{container}@{storage_account}.dfs.core.windows.net/"


# Monter le conteneur Azure dans le système de fichiers Databricks
# Permet d'accéder aux données comme un système de fichiers local
dbutils.fs.mount(
  source = url,
  mountPoint = "/mnt/<mount-name>", #Chemin dans Databricks où le conteneur sera accessible
  extraConfigs = configs)