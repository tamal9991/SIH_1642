document.addEventListener('DOMContentLoaded', function () {
    const profileCard = document.querySelector('.profile-card');

    profileCard.addEventListener('mouseover', function () {
        profileCard.style.transform = 'scale(1.05)';
    });

    profileCard.addEventListener('mouseout', function () {
        profileCard.style.transform = 'scale(1)';
    });
});