let counter = 1;

const myInterval = setInterval(() => {
    console.log(`counter: ${counter++}`)
}, 1000);


setTimeout((ID = myInterval) =>
    clearInterval(ID), 5010);