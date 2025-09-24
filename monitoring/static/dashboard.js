// dashboard.js: Fetch driver status and update dashboard
function updateStatus() {
    fetch('/status/')
        .then(res => res.json())
        .then(data => {
            document.getElementById('face').textContent = data.face_detected ? 'Yes' : 'No';
            document.getElementById('fatigue').textContent = data.fatigue_counter;
            document.getElementById('alert').textContent = data.last_alert;
        });
}
setInterval(updateStatus, 2000);
updateStatus();
