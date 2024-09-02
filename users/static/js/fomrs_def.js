function toggleMenu() {
    const menu = document.getElementById("menuDropdown");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function openProfile() {
    // Add logic to open user profile
    alert('Profile clicked!');
}

function likePost(button) {
    button.textContent = "👍 Liked";
}

function replyPost(button) {
    // Logic to open a reply box
    const replyBox = document.querySelector(".reply-box");
    replyBox.style.display = "block";
}

function sharePost() {
    // Logic to share the post
    alert('Post shared!');
}