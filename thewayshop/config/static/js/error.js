function closeErrorBox() {
    var errorBox = document.getElementById('errorBox');
    errorBox.style.animation = 'slideOut 0.5s forwards'; /* Add slide-out animation */
    errorBox.addEventListener('animationend', function() {
        errorBox.style.display = 'none';
    });
}
