const Canvas01 = document.querySelector("#canvas-01");

(() => {
  if (Canvas01.getContext) {
    var ctx = Canvas01.getContext("2d");

    ctx.fillStyle = "rgb(200, 0, 0)";
    ctx.fillRect(200, 200, 100, 100);

    ctx.fillStyle = "rgba(0, 0, 200, 0.5)";
    ctx.fillRect(250, 250, 100, 100);
  }
})();
