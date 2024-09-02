document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name === "" || email === "" || message === "") {
        alert("Please fill out all fields.");
        return;
    }

    // Display a simple alert with the form data (for demonstration purposes)
    alert(`Name: ${name}\nEmail: ${email}\nMessage: ${message}`);

    // Here you can add AJAX to send the form data to the server or other interaction logic
});
