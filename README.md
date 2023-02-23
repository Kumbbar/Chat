# Chat
## Based on<br>Django - WebSocket - Redis

## Deployment
```
git clone https://github.com/Kumbbar/Chat
cd Chat
cd chat
cp .env.sample .env
- Database and Debug
- vim chat/settings.py
cd ..
sudo docker-compose up
```

## Visual
### Chat
<image height="400" src="https://user-images.githubusercontent.com/90816195/215806736-f3043f98-cf2d-4703-a623-9ba5b21c12f7.png"/>

### List of chats

<image height="300" src="https://user-images.githubusercontent.com/90816195/215807426-79c27390-a898-4861-b285-3ccc8fc956ba.png"/>

## If static files chanched
```
cd chat
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py collectstatic
cp static ../nginx
```
