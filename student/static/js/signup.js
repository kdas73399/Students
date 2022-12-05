
var nam = document.getElementById("name")
var email = document.getElementById("email")
var pass1 = document.getElementById("pass1")
var pass2 = document.getElementById("pass2")
var ph = document.getElementById("ph")

function validname() {

    var fn =nam.ariaValueMax;
    if (isNaN(fn)) {
        nam.className = "success";
        document.getElementById("text").innerHTML = "";

    } else 
    {
        nam.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter name";
    }
}