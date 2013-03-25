// socket.io specific code
var socket = io.connect("");
var count = 0;

socket.on('connect', function () {
    console.log("connected");
    window.setInterval(function() {
        $('#main').append('<p>PING!&nbsp;&nbsp;&nbsp;<i>'+count+'</i>');
        socket.emit('ping',count);
        count += 1;

    }, 1000);
});

socket.on('reconnect', function () {
    console.log("reconnected");
});

socket.on('reconnecting', function () {
    console.log("reconnecting");
});

socket.on('error', function (e) {
    console.log('A unknown error occurred');
});


socket.on('pong', function(e) {
    $('#main').append('&nbsp;&nbsp;&nbsp;PONG!!&nbsp;&nbsp;<i>'+e+'</i></p>');
    console.log("  pong!");
    $('html, body').animate({
            scrollTop: $(document).height()-$(window).height()},
            400,
            "linear"
        );

});


