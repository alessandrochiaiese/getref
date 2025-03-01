document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/api_keys/")
        .then(response => response.json())
        .then(data => {
            console.log("API Keys:", data);
        });
});
