const postal = document.getElementById("id_postal_code");

postal.addEventListener("keyup", (e) => {
  const ptl = document.getElementById("id_postal_code");
  console.log(ptl.value);
  console.log(ptl.value.length);
  let lh = ptl.value.length;
  let vle = ptl.value;
  if ((lh == 2) & (e.keyCode != 8)) {
    console.log(e.target.value);
    e.target.value = e.target.value + "-";
  }
});
