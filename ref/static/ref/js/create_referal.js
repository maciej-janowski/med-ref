let date_input = document.getElementById("id_date_of_issue");

let = n = new Date();
let y = n.getFullYear();
let m = n.getMonth() + 1;
let d = n.getDate();
date_input.value = y + "-" + m + "-" + d;
let counter = 1;

let btn = document.getElementById("adding_button");

btn.addEventListener("click", (e) => {
  e.preventDefault();
  createItem();
});

function createItem() {
  // first argument is where we want the content
  // second is the content
  let html_code = `<li style="margin: 5px auto"><select name='tests_selection_${counter}' style="display: inline" class='selection_element' id='tests_selection_${counter}'>
    
    <option value="">--Please choose a test--</option>
    <option value="ANALITYKA OGÓLNA - Badanie ogólne moczu">ANALITYKA OGÓLNA - Badanie ogólne moczu</option>
    <option value="HEMATOLOGIA - OB">HEMATOLOGIA - OB</option>
    <option value="CHEMIA KLINICZNA - Potas">CHEMIA KLINICZNA - Potas</option>
    <option value="KOAGULOGIA - TT">KOAGULOGIA - TT</option>
    <option value="CHEMIA KLINICZNA - Wapń">CHEMIA KLINICZNA - Wapń</option>
    <option value="CHEMIA KLINICZNA - Profil lipidowy">CHEMIA KLINICZNA - Profil lipidowy</option>
    <option value="CHEMIA KLINICZNA - Triglierydy">CHEMIA KLINICZNA - Triglierydy</option>
    <option value="MARKERY NOWOTWOROWE - AFP">MARKERY NOWOTWOROWE - AFP</option>
    <option value="DIAGNOSTYKA INFEKCJI - Anty HCV">DIAGNOSTYKA INFEKCJI - Anty HCV</option>
    <option value="DIAGNOSTYKA INFEKCJI - Ospa IgG">DIAGNOSTYKA INFEKCJI - Ospa IgG</option>
    <option value="AUTOIMMUNOLOGIA - ANA ELISA">AUTOIMMUNOLOGIA - ANA ELISA</option>
    <option value="ALERGOLOGIA - Zestaw pokarmowy 20">ALERGOLOGIA - Zestaw pokarmowy 20</option>
    <option value="BADANIE MOCZU - Białko w moczu">BADANIE MOCZU - Białko w moczu</option>
    <option value="BADANIE MOCZU - Kreatynina w moczu">BADANIE MOCZU - Kreatynina w moczu</option>
    <option value="ANALITYKA OGÓLNA - Badanie ogólne moczu">ANALITYKA OGÓLNA - Badanie ogólne moczu</option>
    <option value="HEMATOLOGIA - Morfologia krwi">HEMATOLOGIA - Morfologia krwi</option>
    <option value="KOAGULOGIA - Fibrogen">KOAGULOGIA - Fibrogen</option>
    <option value="CHEMIA KLINICZNA - Glukoza">CHEMIA KLINICZNA - Glukoza</option>
    <option value="CHEMIA KLINICZNA - Kreatynina">CHEMIA KLINICZNA - Kreatynina</option>
    <option value="CHEMIA KLINICZNA - ALP">CHEMIA KLINICZNA - ALP</option>
    <option value="CHEMIA KLINICZNA - Amylaza">CHEMIA KLINICZNA - Amylaza</option>
    <option value="CHEMIA KLINICZNA - Triglierydy">CHEMIA KLINICZNA - Triglierydy</option>
    <option value="CHEMIA KLINICZNA - Żelazo">CHEMIA KLINICZNA - Żelazo</option>
    <option value="CHEMIA KLINICZNA - Białko całkowite">CHEMIA KLINICZNA - Białko całkowite</option>
    <option value="MARKERY NOWOTWOROWE - AFP">MARKERY NOWOTWOROWE - AFP</option>
    <option value="ENDOKRYNOLOGIA - Insulina">ENDOKRYNOLOGIA - Insulina</option>
    <option value="ENDOKRYNOLOGIA - Prolaktyna">ENDOKRYNOLOGIA - Prolaktyna</option>
    <option value="DIAGNOSTYKA INFEKCJI - Anty HCV">DIAGNOSTYKA INFEKCJI - Anty HCV</option>
    <option value="DIAGNOSTYKA INFEKCJI - Ospa IgG">DIAGNOSTYKA INFEKCJI - Ospa IgG</option>
    <option value="AUTOIMMUNOLOGIA - ANA ELISA">AUTOIMMUNOLOGIA - ANA ELISA</option>
    <option value="ALERGOLOGIA - Zestaw pokarmowy 20">ALERGOLOGIA - Zestaw pokarmowy 20</option>
    <option value="BADANIE MOCZU - Białko w moczu">BADANIE MOCZU - Białko w moczu</option>
    <option value="BADANIE MOCZU - Kreatynina w moczu">BADANIE MOCZU - Kreatynina w moczu</option>
    <option value="ANALITYKA OGÓLNA - Kał badanie ogólne">ANALITYKA OGÓLNA - Kał badanie ogólne</option>
    <option value="KOAGULOGIA - Fibrogen">KOAGULOGIA - Fibrogen</option>
    <option value="KOAGULOGIA - TT">KOAGULOGIA - TT</option>
    <option value="CHEMIA KLINICZNA - Sód">CHEMIA KLINICZNA - Sód</option>
    <option value="CHEMIA KLINICZNA - Glukoza">CHEMIA KLINICZNA - Glukoza</option>
    <option value="CHEMIA KLINICZNA - Wapń">CHEMIA KLINICZNA - Wapń</option>
    <option value="CHEMIA KLINICZNA - Billirubina całkowita">CHEMIA KLINICZNA - Billirubina całkowita</option>
    <option value="CHEMIA KLINICZNA - ALP">CHEMIA KLINICZNA - ALP</option>
    <option value="CHEMIA KLINICZNA - Profil lipidowy">CHEMIA KLINICZNA - Profil lipidowy</option>
    <option value="CHEMIA KLINICZNA - Triglierydy">CHEMIA KLINICZNA - Triglierydy</option>
    <option value="CHEMIA KLINICZNA - Żelazo">CHEMIA KLINICZNA - Żelazo</option>
    <option value="CHEMIA KLINICZNA - Ferrytyna">CHEMIA KLINICZNA - Ferrytyna</option>
    <option value="CHEMIA KLINICZNA - Albumina">CHEMIA KLINICZNA - Albumina</option>
    <option value="CHEMIA KLINICZNA - Białko całkowite">CHEMIA KLINICZNA - Białko całkowite</option>
    <option value="ENDOKRYNOLOGIA - Progesteron">ENDOKRYNOLOGIA - Progesteron</option>
    <option value="ENDOKRYNOLOGIA - Insulina">ENDOKRYNOLOGIA - Insulina</option>
    <option value="DIAGNOSTYKA INFEKCJI - Anty HCV">DIAGNOSTYKA INFEKCJI - Anty HCV</option>
    <option value="ALERGOLOGIA - Zestaw pokarmowy 20">ALERGOLOGIA - Zestaw pokarmowy 20</option>
    <option value="ALERGOLOGIA - Zestaw wziewny 20">ALERGOLOGIA - Zestaw wziewny 20</option>
</select>
<button class="btn btn-danger" style="display:inline-block" onClick="deleteItem(this)">Delete</button></li>`;
  btn.insertAdjacentHTML("beforebegin", html_code);
  counter++;
}

function deleteItem(elementToDelete) {
  elementToDelete.parentElement.remove();
  counter--;
}

// btn.insertAdjacentHTML("beforebegin", html_code);

// let ourForm = document.getElementById("ourForm");
// let ourField = document.getElementById("ourField");
// let ourList = document.getElementById("ourList");

// ourForm.addEventListener("submit", (e) => {
//   e.preventDefault();
//   createItem(ourField.value);
// });

// function createItem(item) {
//   // first argument is where we want the content
//   // second is the content
//   let ourHTML = `<li>${item}<button onClick="deleteItem(this)">Delete</button></li>`;
//   ourList.insertAdjacentHTML("beforeend", ourHTML);
//   ourField.value = "";
//   ourField.focus();
// }

// function deleteItem(elementToDelete) {
//   elementToDelete.parentElement.remove();
// }
