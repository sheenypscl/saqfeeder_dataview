// start button for phSensor calibration
document.getElementById('calibrate-ph-btn').addEventListener('click', function() {
      document.getElementById('result').innerText = 'Calibrating... please wait ⏳';
      fetch('/api/calibrate/acid/')
        .then(res => res.json())
        .then(data => {
          document.getElementById('result').innerText = data.message;
        })
        .catch(err => {
          document.getElementById('result').innerText = 'Error: ' + err;
        });
    });

// start button for DO calibration
document.getElementById('calibrate-do-btn').addEventListener('click', function() {
      document.getElementById('result-do').innerText = 'Calibrating... please wait ⏳';
      fetch('/api/calibrate/do/')
        .then(res => res.json())
        .then(data => {
          document.getElementById('result-do').innerText = data.message;
        })
        .catch(err => {
          document.getElementById('result-do').innerText = 'Error: ' + err;
        });
    }); 
    
 // start button for EC calibration
document.getElementById('calibrate-ec-btn').addEventListener('click', function() {
      document.getElementById('result-ec').innerText = 'Calibrating... please wait ⏳';
      fetch('/api/calibrate/ec/')
        .then(res => res.json())
        .then(data => {
          document.getElementById('result-ec').innerText = data.message;
        })
        .catch(err => {
          document.getElementById('result-ec').innerText = 'Error: ' + err;
        });
    });    



// calibration sequence logic
function showStep(step) {
  document.querySelectorAll("#calibration-container > div").forEach(div => div.style.display = "none");
  document.getElementById(`step-${step}`).style.display = "block";
}

function skipAll() {
  showStep('done');
}

function finishCalibration() {
  showStep('done');
}

function runCalibration(sensor) {
  const output = document.getElementById(`${sensor}-output`);
  const startBtn = document.getElementById(`${sensor}-start`);
  const skipBtn = document.getElementById(`${sensor}-skip`);

  output.textContent = "Running calibration... please wait.";
  startBtn.disabled = true;
  skipBtn.disabled = true;

  fetch(`/api/calibrate/${sensor}/`)
    .then(res => res.json())
    .then(data => {
      if (data.result) {
        output.textContent = data.result;
      } else {
        output.textContent = "Error: " + data.error;
      }
      const next = sensor === "ph" ? "do" : sensor === "do" ? "ec" : "done";
      const nextBtn = document.createElement("button");
      nextBtn.textContent = next === "done" ? "Finish" : "Next";
      nextBtn.className = "btn btn-primary mt-3";
      nextBtn.onclick = () => showStep(next);
      output.insertAdjacentElement("afterend", nextBtn);
    })
    .catch(err => {
      output.textContent = "Error: " + err;
    });
}    


// proceed with collection data table
function openCSVViewer() {
  window.location.href = '/api/csv/';
}