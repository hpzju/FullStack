// import moment from "moment";

const displayClock = () => {
  let el = document.getElementById("clock");
  el.innerHTML = moment().format("MMMM Do YYYY, h:mm:ss SSS a");
};

const updateClock = () => {
  displayClock();
  setTimeout(updateClock, 1000);
};

updateClock();
