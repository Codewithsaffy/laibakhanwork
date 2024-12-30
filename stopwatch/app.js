let start_timer = document.querySelector(".start");
let stop_timer = document.querySelector(".stop");
let reset_timer = document.querySelector(".reset");
let time = document.querySelector(".time");

let msec = 0;
let ssec = 0;
let min = 0;
let timeId = null;

start_timer.addEventListener('click', function () { // Corrected 'addEventListener'
  if (timeId !== null) {
    clearInterval(timeId);
  }
  timeId = setInterval(startTimer, 10);
});

stop_timer.addEventListener('click', function () { // Corrected 'addEventListener'
  clearInterval(timeId);
});

reset_timer.addEventListener('click', function () { // Corrected 'addEventListener'
  clearInterval(timeId);
  time.innerHTML = `00 : 00 : 00`;
  msec = 0; // Reset milliseconds
  ssec = 0; // Reset seconds
  min = 0;  // Reset minutes
});

function startTimer() {
  msec++;
  if (msec == 100) { // Increment seconds after 100 milliseconds
    msec = 0;
    ssec++;
    if (ssec == 60) { // Increment minutes after 60 seconds
      ssec = 0;
      min++;
    }
  }

  let msecString = msec < 10 ? `0${msec}` : msec;
  let ssecString = ssec < 10 ? `0${ssec}` : ssec;
  let minString = min < 10 ? `0${min}` : min;

  time.innerHTML = `${minString} : ${ssecString} : ${msecString}`; // Fixed format
}
