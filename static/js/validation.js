function validateEmail() {
    const emailInput = document.getElementById('email');
    const emailError = document.getElementById('emailError');
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(emailInput.value)) {
        emailError.textContent = 'Please enter a valid email address.';
        return false;
    }

    emailError.textContent = '';
    return true;
}
