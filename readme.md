# Django Firebase

---

This vanilla Django Project contains an App 
called django_firebase which implements Firebase Cloud 
Messaging for web/browser (API V1 not Legacy). In theory, a
setup such as this should be fairly simple but the getting
everything configured was tedious hence this project and
detailed instructions.

The App is intended to be portable (i.e integrate in 
your project) once you've tested the basic functionality in 
confirmed all the Firebase requirements have been met.

# Todos

---

- Add support for mobile (iOS / Android)
- Add lifecycle to FCMUserToken to invalidate when Firebase respondes with 'Bad Token'
- Build as a pip installable module and list on pypi
- Figure out how to identify when the Firebase Service Worker has failed/timed out and restart
- 


# Setup
___
Log into Firebase  
Create a Firebase Project  
Add a Web App to the Project  
`Note: the script values will be needed for the .env below later`

Go to Project > Project Settings > Cloud Messaging   
Click 'Generate key pair' under Web Push certificates  

`Note: the public key of the key pair == FCM_VAPID_KEY later`  

Go to Project > Project Settings > Cloud Messaging  
Click 'Manage Service Accounts'  
Click Firebase Service Account with your project name in it  
Confirm the Service Account is 'Enabled'  

`Note the Service Account / Unique id == FCM_CLIENT_ID later`

Click 'KEYS'  
Click 'ADD KEY'  
Click 'Create new key'  
Select 'JSON'  
Click 'Create'  

`Note: the downloaded json file contains the Private and Public keys 
needed to complete the .env configuration.`


Update the following the .env values from above
```
FCM_API_KEY=[FIREBASE_API_KEY]
FCM_AUTH_DOMAIN=[FIREBASE_AUTH_DOMAIN]
FCM_PROJECT_ID=[FIREBASE_PROJECT_ID]
FCM_STORAGE_BUCKET=[FIREBASE_STORAGE_BUCKET]
FCM_MESSAGING_SENDER_ID=[FIREBASE_MESSAGING_SENDER_ID]
FCM_APP_ID=[FIREBASE_APP_ID]
FCM_MEASUREMENT_ID=[FIREBASE_MEASUREMENT_ID]
FCM_VAPID_KEY=[FIREBASE_VAPID_KEY]
FCM_PRIVATE_KEY_ID=[FIREBASE_PRIVATE_KEY_ID]
FCM_PRIVATE_KEY=[FIREBASE_PRIVATE_KEY]
FCM_CLIENT_ID=[FIREBASE_CLIENT_ID]
FCM_BASE_URL=https://fcm.googleapis.com
FCM_SCOPES=https://www.googleapis.com/auth/firebase.messaging
FCM_MESSAGE_ICON=[https://website.com/path-to-logo.png]
FMC_MAX_NOTIFICATIONS_PER_USER=3
```

Note: Web notifications require a Django authenticated user to accept 
notifications at the browser level. 

TBD

# Management Commands
 
___

TBD

# Tests
 
___