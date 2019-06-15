//model
class Expense {
  constructor(description, amount) {
    this.description = description;
    this.cost = amount;
  }

  toItem() {
    return { description: this.description, cost: this.cost };
  }

  isValid() {
    return !!this.description && !!this.cost;
  }
}

class Budget {
  constructor(budget) {
    this.total = budget;
    this.left = budget;
    this.budgetLists = [];
  }
  isAllowed(expense) {
    return this.left >= expense.cost;
  }
  expend(expense) {
    this.left -= expense.cost;
    this.budgetLists.push(expense.toItem());
  }
}

const budget = new Budget(1000);

//view
const totalBudget = document.querySelector("#total");
const leftBudeget = document.querySelector("#left");
const expenseList = document.querySelector("#expenses ul");
const form = document.querySelector("#add-expense");

function updateBudgetView(expense) {
  leftBudeget.textContent = budget.left.toFixed(2);

  const li = document.createElement("li");
  li.className =
    "list-group-item d-flex justify-content-between align-items-center";
  // Create the template
  li.innerHTML = `
       ${expense.description}
       <span class="badge badge-primary badge-pill">$ ${expense.cost}</span>
  `;

  // Insert into the HTML
  expenseList.appendChild(li);
}

//control
//event handlers
const formSubmit = ev => {
  ev.preventDefault();
  const description = document.querySelector("#expense");
  const amount = document.querySelector("#amount");
  const expense = new Expense(description.value, Number(amount.value));

  if (expense.isValid()) {
    if (budget.isAllowed(expense)) {
      budget.expend(expense);
      updateBudgetView(expense);
    } else {
      alert("Run out of budget!");
    }
  } else {
    alert("Please input valid expense name and amount!");
  }
};

const initBudget = () => {
  totalBudget.textContent = budget.total.toFixed(2);
  leftBudeget.textContent = budget.left.toFixed(2);
};

//event listeners
(() => {
  document.addEventListener("DOMContentLoaded", initBudget);
  form.addEventListener("submit", formSubmit);
})();
