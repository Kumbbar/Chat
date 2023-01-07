var chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + currentUser + '/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    console.log(data)
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed');
};
