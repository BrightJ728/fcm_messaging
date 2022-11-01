from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()
origins = [
 
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]


import fcm_manager as fcm
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/token/")
async def send_notification_by_token(token_list:list, msg_title: str, msg_body: str):
    response=fcm.sendPush(token_list, msg_title, msg_body)
    return response
   
@app.post("/topic/")
async def subscribe_topic_message(topic:str, tokens: list):
    response=fcm.subscribe_topic(tokens, topic)
    return response

@app.post("/topic/unsubscribe/")
async def unsubscribe_topic_message(topic:str, tokens:list):
    response=fcm.unsubscribe_topic(tokens, topic)
    return response
   

@app.post("/topic/send/")
async def send_topic_message(topic: str, msg_title: str, msg_body: str):
    response=fcm.send_topic(topic, msg_title, msg_body)
    return response

@app.post("/topic/bulk/")
async def send_bulk_messages(token: str):
    response=fcm.send_batch_of_messages(token) 
    return response

@app.post("/")
async def root():
    url= "https://iid.googleapis.com/iid/v1:batchAdd"
    headers = {
    "Content-Type":"application/json",
    "Authorization":"key=BNMnywVZ2E8_-spIaTQDDk8HnO_U7E9i8H7lzHE5eev061egrsLogD_gN-kl-0Uu22yXc5YGfSgFz-PVMoUOQiA"
    }
    mess={
    "to": "/topics/movies",
    "registration_tokens": ["nKctODamlM4:CKrh_PC8kIb7O...", "1uoasi24:9jsjwuw...", "798aywu:cba420..."],
    }
    response = requests.post(url, headers=headers, data=mess)

