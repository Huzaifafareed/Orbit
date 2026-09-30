const API_URL = "http://127.0.0.1:5000";


async function loadStatus() {

    const response = await fetch(API_URL + "/status");

    const data = await response.json();

    updateScreen(data);
}


async function addComponent(component) {

    const response = await fetch(API_URL + "/add-component", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            component: component
        })
    });

    const data = await response.json();

    updateScreen(data);

    document.getElementById("message").textContent =
        component + " added to spacecraft!";
}


function updateScreen(data) {

    document.getElementById("mass").textContent =
        data.mass;

    document.getElementById("power").textContent =
        data.power;

    document.getElementById("science").textContent =
        data.science;
}


loadStatus();