$(document).ready(function() {
    $(document).on('click','#submitRegistration',function() {
        var email = $('#email').val();
        var password = $('#password').val();
        var first_name = $('#first-name').val();
        var last_name = $('#last-name').val();
        var username = $('#username').val();
        // Data to be passed
        var userData = {
            email: email,
            password: password,
            first_name: first_name,
            last_name: last_name,
            username: username,
        };
        
        // Set a cookie named "user_info" with JSON data, expiring in 7 days
        $.cookie('user_info', JSON.stringify(userData), { expires: 7, path: '/opt_verify' });

        // Redirect to the next page
        window.location.href = "/submitRegistration";
    });
});

