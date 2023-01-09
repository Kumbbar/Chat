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
