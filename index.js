// =============Navbar=================
var navbar = document.getElementById("navBar");
var btns = navbar.getElementsByClassName("navbar_btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

// =============From==============
const form = document.querySelector('form');
const urlInput = form.querySelector('#url');
const errorLabel = form.querySelector("#error-label");
const formClear = form.querySelector("#form-clear");

form.addEventListener('submit', (event) => {
    if (urlInput.value.trim() === '') {
        event.preventDefault(); // prevent form submission
        urlInput.classList.add('error');
        formClear.classList.add('error-right');
        errorLabel.classList.remove('error-label-remove');
        errorLabel.classList.add('error-label-add');
        urlInput.focus();
    }
});

//===================================
function clearInput() {
    const urlInput = form.querySelector('#url');
    urlInput.value = '';
    urlInput.focus();
}