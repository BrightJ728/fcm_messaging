# from firebase_admin import credentials, messaging
# from fcm_manager import credentials_init
# cred = credentials.Certificate('service-account.json')
    
# credent=firebase_admin.initialize_app(cred)
# firebase_admin.initialize_app(cred)

# def sendPush(title, msg, registration_token, dataObject=None):
#     # See documentation on defining a message payload.
#     message = messaging.MulticastMessage(
#         notification=messaging.Notification(
#             title=title,
#             body=msg
#         ),
#         data=dataObject,
#         tokens=registration_token,
#     )

#     # Send a message to the device corresponding to the provided
#     # registration token.
#     response = messaging.send_multicast(message)
#     # Response is a message ID string.
#     print('Successfully sent message:', response)