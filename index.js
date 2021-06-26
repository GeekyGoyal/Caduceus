const socket = io.connect();
var form = document.getElementById("form");
var messages = document.getElementById("messages");
var input = document.getElementById("message-box");
var isDoctor = false;
var roomNumber = -1;

function getPerson() {
    let answer = prompt("Type \"yes\" if you are a doctor").toLowerCase();
    if (answer === "yes") {
        isDoctor = true;
        socket.emit("person", "doctor");
    } else {
        socket.emit("person", "patient");
    }
}

socket.on("chat message", (msg) => {
    var item = document.createElement("div");
    item.className = "message";
    item.textContent = msg;
    
    messages.appendChild(item);
    window.scrollTo(0, document.body.scrollHeight);
});

socket.on("number", (num) => {
    roomNumber = num;
});

form.addEventListener("submit", (e) => {
    e.preventDefault();
    if(input.value) {
        socket.emit("chat message", `${roomNumber}~~~${isDoctor}~~~${input.value}`);
        input.value="";
    }
});