function optimize() {

    fetch("http://127.0.0.1:5000/optimize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            distance: document.getElementById("distance").value,
            users: document.getElementById("users").value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText =
            "Optimized Power: " + data.optimized_power;
    })
    .catch(error => {
        console.log("Error:", error);
    });
}