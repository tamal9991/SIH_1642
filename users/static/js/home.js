function redirectToPage() {
    window.location.href = "/login_def"; // Replace with the desired URL
}

function redirectToRes(){
    window.location.href = "/res"; // Replace with the desired URL
}

function LogoutIndex(){
    window.location.href = "/logout";
}
function navigate(e){
    console.log(e);
    window.location.href = e;
}
function redirectDFS(){
    window.location.href = "/domain_form_stack";
}

document.addEventListener('DOMContentLoaded', function () {
    const viewProfile = document.getElementById('view-profile');
    const settings = document.getElementById('settings');
    const logout = document.getElementById('logout');

    logout.addEventListener('click', function () {
        alert('Logout clicked');
        // Add functionality to logout
    });
});


// ajax for chart bot

$(document).on('click', '#send-button', function() {
    const userInput = document.getElementById('user-input').value;
    console.log("User input:", userInput);
    
    $.ajax({
        url: "/chart_bot/",  // URL should match the Django URL pattern
        type: "GET",
        data: {
            data: userInput,
        },
        success: function(response) {
            $('#user-input').val('')
            var sender = 'User';
            var message = response.data;
            const chatContent = document.getElementById("chat-content");
            const messageBubble = document.createElement("div");
            messageBubble.classList.add("chat-bubble", sender === "user" ? "user-message" : "bot-message");
            messageBubble.textContent = message;
            chatContent.appendChild(messageBubble);
            chatContent.scrollTop = chatContent.scrollHeight;
        },
        error: function(xhr, errmsg, err) {
            console.log('Error:', errmsg);
        }
    });
});


