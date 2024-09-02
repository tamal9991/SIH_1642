document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("chat-toggle").addEventListener("click", toggleChat);
    
    document.getElementById("user-input").addEventListener("keypress", function(event) {
    
    
    
    });
});

function toggleChat() {
    const chatBody = document.getElementById("chat-body");
    if (chatBody.style.display === "none" || chatBody.style.display === "") {
        chatBody.style.display = "flex";
    } else {
        chatBody.style.display = "none";
    }
}


