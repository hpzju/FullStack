const scriptInjection = type => {
  let el = document.createElement("script");
  el.src = `./js/${type}.js`;
  document.body.appendChild(el);
};

const featureCheck = () => {
  try {
    eval("`string template literal`;");
  } catch (err) {
    return false;
  }
  return true;
};

if (featureCheck()) {
  scriptInjection(`ES6`);
} else {
  scriptInjection("ES5");
}
