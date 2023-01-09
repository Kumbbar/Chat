var chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + interlocutor + '/');

window.onload=function(){
     window.scrollTo(0,document.body.scrollHeight);
}

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    // document.querySelector('#chat-log').value += (message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};


document.querySelector('#chat-message-submit').onclick = function(e) {
    chatSocket.send(JSON.stringify({
        'message': 'message',
        'sender': currentUser,
        'receiver': interlocutor
    }));

};