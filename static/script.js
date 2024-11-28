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
  