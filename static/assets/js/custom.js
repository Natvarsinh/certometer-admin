document.addEventListener("DOMContentLoaded", function() {
    // Get the current URL path
    var currentPath = window.location.pathname;

    // Select the navigation items
    var navItems = document.querySelectorAll('#myNavbar .nav-link');

    var dropdownItems = document.querySelectorAll(".dropdown-item");
    
    dropdownItems.forEach(function(item) {
        var href = item.getAttribute('href');
        // Check if the current URL path matches the href attribute
        if (currentPath === href) {
            // Add the "active" class to the matching navigation item
            item.classList.add('active');
            var parentDropdown = item.closest('.dropdown-menu');
            var parentDropdownSub = item.closest('.subDropdownMenu');
            var parentLI = item.closest('.nav-item');
            parentDropdown.classList.add('show');
            if(parentDropdownSub != undefined){
                parentDropdownSub.classList.add('show');
            }
            parentLI.classList.add("active");
        }
    });

    // Loop through each navigation item
    navItems.forEach(function(item) {
        // Get the href attribute of the navigation item
        if (item.parentElement.tagName.toLowerCase() === 'li'){

            var href = item.getAttribute('href');
            // Check if the current URL path matches the href attribute
            if (currentPath === href) {
                // Add the "active" class to the matching navigation item
                item.parentElement.classList.add('active');
            }
        }
    });
});