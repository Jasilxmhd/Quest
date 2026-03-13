let display = document.getElementById("display");

function add(value) {
  display.value = display.value + value;
}

function calculate() {
  try {
    
    let sanitized = display.value.replace(/÷/g, "/");
    display.value = eval(sanitized);
  } catch {
    display.value = "Error";
  }
}

function clearall() {
  display.value = "";
}

function backspace() {
  display.value = display.value.slice(0, -1);
}