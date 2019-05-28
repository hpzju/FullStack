const featureCheck = () => {
  try {
    eval("`string template literal`;");
  } catch (err) {
    return false;
  }
  return true;
};

// const userAgent = navigator.userAgent;

// if (userAgent.includes("Chrome")) {
//   console.log(`Hello from ES6.`);
// } else {
//   console.log(`Hello from ES5.`);
// }

if (featureCheck()) {
  console.log(`Hello from ES6 with featureCheck().`);
} else {
  console.log(`Hello from ES5 with featureCheck().`);
}
