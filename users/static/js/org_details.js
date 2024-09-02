document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Simple form validation
    var companyName = document.getElementById('companyName').value;
    var owner = document.getElementById('owner').value;
    var email = document.getElementById('email').value;
    var phoneNumber = document.getElementById('phoneNumber').value;

    if (companyName && owner && email && phoneNumber) {
        // Show confirmation message
        document.getElementById('confirmationMessage').classList.remove('hidden');
        // Reset form
        this.reset();
    } else {
        alert('Please fill in all required fields.');
    }
});