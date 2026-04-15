function submitNetwork() {

    fetch("http://127.0.0.1:5000/network", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            bandwidth: document.getElementById("bandwidth").value,
            latency: document.getElementById("latency").value,
            signal: document.getElementById("signal").value,
            users: document.getElementById("users").value,
            slice: localStorage.getItem("slice")
        })
    })

    .then(response => response.json())

    .then(data => {
        document.getElementById("result").innerText =
            data.message + " | Priority: " + data.priority;
    })

    .catch(error => {
        console.error("Network Error:", error);
    });
}