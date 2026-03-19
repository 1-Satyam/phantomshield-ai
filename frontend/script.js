let chart;

async function getData() {
    const rain = document.getElementById("rain").value;
    const traffic = document.getElementById("traffic").value;
    const area = document.getElementById("area").value;
    const fraud = document.getElementById("fraudToggle").checked;

    const res = await fetch("http://127.0.0.1:5000/get_insurance_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            rain_mm: parseFloat(rain),
            traffic: traffic,
            area: area
        })
    });

    const data = await res.json();

    let trust = data.trust_score;

    if (fraud) {
        trust = (trust * 0.3).toFixed(2);
        data.status = "FLAGGED";
    }

    document.getElementById("risk").innerText = data.risk_score;
    document.getElementById("trust").innerText = trust;
    document.getElementById("premium").innerText = data.premium;

    const statusEl = document.getElementById("status");
    statusEl.innerText = data.status;
    statusEl.className = "";

    if (data.status === "APPROVED") {
        statusEl.classList.add("approved");
    } else {
        statusEl.classList.add("flagged");
    }

    document.getElementById("riskBar").style.width = (data.risk_score * 100) + "%";
    document.getElementById("trustBar").style.width = (trust * 100) + "%";

    document.getElementById("w").innerText = data.debug.weather;
    document.getElementById("t").innerText = data.debug.traffic;
    document.getElementById("l").innerText = data.debug.location;
    document.getElementById("b").innerText = data.debug.behavior;

    updateChart(data.risk_score, trust);
}

function updateChart(risk, trust) {
    const ctx = document.getElementById("chart");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Risk", "Trust"],
            datasets: [{
                label: "Score",
                data: [risk, trust]
            }]
        }
    });
}