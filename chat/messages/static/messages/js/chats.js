var chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + currentUser + '/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    var unread_messages = document.getElementById(data["sender"]).textContent;
    document.getElementById(data["sender"]).textContent = Number(unread_messages) + 1 + ''
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed');
};

var buttons = document.getElementsByClassName('btn-chat');

for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function (e) {
        var btn_id = e.target.id.toString()
        document.getElementById(btn_id.substring(0, btn_id.length -4)).textContent = '0'
    });
}