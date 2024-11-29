'use strict';

document.getElementById('profileMenuToggle').addEventListener('click', function() {
    const menu = document.getElementById('menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
});

// Close the menu when clicking outside
window.addEventListener('click', function(event) {
    const menu = document.getElementById('menu');
    const profilePic = document.getElementById('profileMenuToggle');
    if (event.target !== menu && !menu.contains(event.target) && 
        event.target !== profilePic && !profilePic.contains(event.target)) {
        menu.style.display = 'none';
    }
});


//==========================================================
//----------------------Create Quote Script------------------------
//==========================================================

// Add event listener for focus
document.querySelectorAll('input').forEach(function(input) {
    input.addEventListener('focus', function() {
        this.closest('.form-group').classList.add('focused');
    });
});

// Add event listener for blur
document.querySelectorAll('input').forEach(function(input) {
    input.addEventListener('blur', function() {
        var inputValue = this.value;
        if (inputValue === "") {
            this.classList.remove('filled');
            this.closest('.form-group').classList.remove('focused');
        } else {
            this.classList.add('filled');
        }
    });
});
