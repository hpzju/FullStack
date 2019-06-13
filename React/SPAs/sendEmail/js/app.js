//vars
const emailRE = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
let email = document.querySelector("#email");
let subject = document.querySelector("#subject");
let message = document.querySelector("#message");
let sendEmailForm = document.getElementById("email-form");

let sendBtn = document.querySelector("#sendBtn");
let resetBtn = document.querySelector("#resetBtn");

//validation

const validate = () => {
  sendBtn.disabled = true;
  if (subject.value && message.value && emailRE.test(email.value)) {
    sendBtn.disabled = false;
  }
};

validate();

//events

(() => {
  email.addEventListener("blur", ev => {
    validate();
  });
  subject.addEventListener("blur", ev => {
    validate();
  });
  message.addEventListener("blur", ev => {
    validate();
  });

  sendEmailForm.addEventListener("submit", sendEmail);

  resetBtn.addEventListener("click", ev => {
    email.value = null;
    subject.value = null;
    message.value = null;
    sendBtn.disabled = true;
  });
})();

//send email
function sendEmail(e) {
  e.preventDefault();

  // show the spinner
  const spinner = document.querySelector("#spinner");
  spinner.style.display = "block";

  // Show the image
  const sendEmailImg = document.createElement("img");
  sendEmailImg.src = "img/mail.gif";
  sendEmailImg.style.display = "block";

  // Hide Spinner then show the send Email image
  setTimeout(function() {
    // Hide the spinner
    spinner.style.display = "none";

    // Show the image
    document.querySelector("#loaders").appendChild(sendEmailImg);

    // After 5 seconds, hide the image and reset the form
    setTimeout(function() {
      sendEmailForm.reset();
      sendEmailImg.remove();
    }, 5000);
  }, 3000);
}
//reset
