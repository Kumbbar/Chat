var chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + interlocutor + '/');

var chatSocketGet = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + currentUser + '/');

chatSocketGet.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    var sender = data['sender'];

    if(sender != interlocutor) { return }

    let new_received_message = document.createElement('div');
    new_received_message.innerHTML = `
        <div class="msg-block">
            <p class="msg msgTextReceiver">` + message +
            `<br><span class="msgTime">только что</span></p>
        </div>
    `
    messages.prepend(new_received_message)
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};


document.querySelector('#chat-message-submit').onclick = function(e) {
    if(document.getElementById('inputTxt').value != ''){
            chatSocket.send(JSON.stringify({
            'message': document.getElementById('inputTxt').value,
            'sender': currentUser,
            'receiver': interlocutor
        }));
        let new_send_message = document.createElement('div');
        new_send_message.innerHTML = `
            <div class="msg-block">
                <p class="msg msgTextSender">` + document.getElementById('inputTxt').value +
                `<br><span class="msgTime">только что</span></p>
            </div>
        `
        messages.prepend(new_send_message)
        document.getElementById('inputTxt').value = ''
    }
};