const alert = e => console.log(e);

const promise = new Promise(function (resolve, reject) {
    setTimeout(() => resolve(1), 4000);
  })
  .then(function (result) {
    alert(result);
    return result * 3;
  })
  .then(function (result) {
    alert(result);
    return result * 4;
  })
  .then(function (result) {
    alert(result);
    return result * 6;
  });

console.log(promise);
console.log(promise.then(alert));

async function firstAsync() {
  let promise = new Promise((res, rej) => {
    setTimeout(() => res("Now it's done!"), 2000);
  });

  // wait until the promise returns us a value
  let result = await promise;

  // "Now it's done!"
  alert(result);
}

firstAsync();

function firstSync() {
  let promise = new Promise((res, rej) => {
    setTimeout(() => res("Now it's done! in Sync"), 1000);
  });

  // not wait the promise returns us a value
  let result = promise;

  // "Now it's done!"
  alert("in first Sync");
  alert(typeof result, result);
}

firstSync();