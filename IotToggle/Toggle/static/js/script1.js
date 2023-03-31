var myCheckbox = document.getElementById("toggle");

myCheckbox.addEventListener('change', function() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url "my_view" %}');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Checkbox value saved successfully!');
        } else {
            console.log('There was an error saving the checkbox value.');
        }
    };
    xhr.send(JSON.stringify({ 'myCheckbox': this.checked }));
});
