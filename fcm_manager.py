import firebase_admin

from firebase_admin import credentials, messaging
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)

def sendPush(token_list, msg_title, msg_body):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=msg_title,
            body=msg_body
        ),
        data=None,
        tokens=token_list,
    )

    response = messaging.send_multicast(message)
    # Response is a message ID string.
    return response

def subscribe_topic(tokens:list, topic:str):
    # These registration tokens come from the client FCM SDKs.
    response = messaging.subscribe_to_topic(tokens, topic)
    return response 

def unsubscribe_topic(tokens:list, topic:str):
    # These registration tokens come from the client FCM SDKs.
    response = messaging.unsubscribe_from_topic(tokens, topic)
    return response 

def  send_messages_single_devices(registration_token:str, msg_title: str, msg_body: str):
    message = messaging.Message(
        notification={
            'title': msg_title,
            'body': msg_body,
        },
        token=registration_token,
    )
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

def send_messages_multiple_devices(registration_tokens:list):
    # Create a list containing up to 500 registration tokens.
# These registration tokens come from the client FCM SDKs.


    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)

    print('{0} messages were sent successfully'.format(response.success_count))

def send_batch_of_messages(token:str):
    # Create a list containing up to 500 messages.
    messages = [
        messaging.Message(
            notification=messaging.Notification('Price drop', '5% off all electronics'),
            token=token,
        ),
        # ...
        messaging.Message(
            notification=messaging.Notification('Price drop', '2% off all books'),
            topic='news',
        ),
    ]


    response = messaging.send_all(messages)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))
    
    return response


def send_topic(topic: str, msg_title: str, msg_body: str):
    message = messaging.Message(
        notification=messaging.Notification(
            title=msg_title,
            body=msg_body
        ),
        data=None,
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    
    print('Successfully sent message:', response)
    return response

