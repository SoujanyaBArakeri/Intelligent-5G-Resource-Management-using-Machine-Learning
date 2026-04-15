function login() {

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    })

    .then(response => response.json())

    .then(data => {

        // Show login message
        document.getElementById("message").innerText = data.message;

        // ✅ Store Role + Network Slice
        if (data.role && data.slice) {

            localStorage.setItem("role", data.role);
            localStorage.setItem("slice", data.slice);

            // Redirect to dashboard
            window.location.href = "dashboard.html";
        }
    })

    .catch(error => {
        console.error("Login Error:", error);
    });
}