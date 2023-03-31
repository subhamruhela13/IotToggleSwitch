var myCheckbox = document.getElementById("toggle");

myCheckbox.addEventListener('change', function() {
    if (this.checked) {
        console.log('Checkbox is checked');
        // Do something when the checkbox is checked
    } else {
        console.log('Checkbox is unchecked');
        // Do something when the checkbox is unchecked
    }
});
