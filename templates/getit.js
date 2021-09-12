function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");

  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});

//Referencia: https://www.washington.edu/accesscomputing/webd2/student/unit5/module2/lesson5.html

function change_update() {
  var change = document.getElementById('update_js');
  var bttn = document.getElementById('btn_edit');
  // get the current value of the clock's display property
  var displaySetting = change.style.display;


  // now toggle the clock and the button text, depending on current state
  if (displaySetting == 'flex') {
    // clock is visible. hide it
    change.style.display = 'none';
    bttn.innerHTML = "Editar"
  }
  else {
    // clock is hidden. show it
    change.style.display = 'flex';
    // change button text
    bttn.innerHTML = "Cancelar"
  }
};

document.getElementById("btn_change").addEventListener("click", change_update);