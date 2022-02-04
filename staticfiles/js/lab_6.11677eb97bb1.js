$(document).ready(function(){
    $(".chat-text").keypress(function(event) {
        if (event.which === 13) {
            var chat = $("textarea").val();
            $("textarea").val("");
            $(".msg-insert").append('<p class="msg-send">'+input+'</p>');
            $(".msg-insert").append('<br>');
        }
    });
});
