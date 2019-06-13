// vars
const form = document.querySelector("#request-quote");
const result = document.getElementById("result");
const maker = ["", "USA", "Asia", "EU"];

//events
(() => {
  //handle year options display
  document.addEventListener("DOMContentLoaded", ev => {
    const selectYears = document.querySelector("#year");
    let year = new Date().getFullYear();

    //init select options
    const optionItem = document.createElement("option");
    optionItem.textContent = "-Select-";
    selectYears.appendChild(optionItem);

    for (let i = year; i > year - 15; i--) {
      const optionItem = document.createElement("option");
      optionItem.value = i;
      optionItem.textContent = String(i);
      selectYears.appendChild(optionItem);
    }
  });

  //handle form summit
  form.addEventListener("submit", ev => {
    ev.preventDefault();

    // Read the values from the FORM
    const make = maker[document.getElementById("make").value || 0];
    const year = document.getElementById("year").value;
    // Read the radio buttons
    const level = document.querySelector('input[name="level"]:checked').value;

    // Check that all the fields have something
    if (make === "" || year === "" || level === "") {
      alert("All field is mandatory, please select!");
    } else {
      // Clear the previous quotes

      const prevResult = document.querySelector("#result div");
      if (prevResult != null) {
        prevResult.remove();
      }

      const price = Number(Math.random() * 5000).toFixed(2);

      // Print the result from HTMLUI();
      // Insert the result
      const div = document.createElement("div");
      div.innerHTML = `
     <p class="header">Summary</p>
     <p>Make: ${make}</p>
     <p>Year: ${year}</p>
     <p>Level: ${level}</p>
     <p class="total">Total: $ ${price}</p>
     `;

      const spinner = document.querySelector("#loading img");
      spinner.style.display = "block";

      setTimeout(function() {
        spinner.style.display = "none";
        // Insert this into the HTML
        result.appendChild(div);
      }, 1000);
    }
  });
})();
