$(document).ready(function() {
    $("#send-button").click(function() {
        var userInput = $("#user-input").val();
        if (userInput.trim() !== "") {
            $("#chat-box").append("<p class='user'>" + userInput + "</p>");
            $("#user-input").val("");

            $.post("/get_response", {user_input: userInput}, function(data) {
                $("#chat-box").append("<p class='bot'>" + data.response + "</p>");
                $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);
            });
        }
    });

    $("#user-input").keypress(function(event) {
        if (event.which == 13) {
            $("#send-button").click();
        }
    });
});
