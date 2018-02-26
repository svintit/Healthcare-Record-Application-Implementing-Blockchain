// Get the modal
var modalExist = document.getElementById('myModalExist');
var modalNew = document.getElementById('myModalNew')

// Get the button that opens the modal
var btnExist = document.getElementById("existingPatient");
var btnNew = document.getElementById("newPatient");

// Get the <span> element that closes the modal
var spanExist = document.getElementsByClassName("closeExist")[0];
var spanNew = document.getElementsByClassName("closeNew")[0];

spanExist.onclick = function() {
   modalExist.style.display = "none";
}


// When the user clicks on the button, open the modal
btnExist.onclick = function() {
   modalExist.style.display = "block";
}

btnNew.onclick = function() {
   modalNew.style.display = "block";
}

// When the user clicks on <span> (x), close the modal

var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.name = "John Doe";
});

function patientLogIn(){
   var patient = document.getElementById("patientUser").value;
   var patientPass = document.getElementById("patientPswd").value;
   if (patient == "patient" && patientPass =="a"){
      return true
   }
   else{
      alert("Login Invalid - Try again");
   }
   return false;
}

//Tab functions
function openRecord(opt, name){
   var i, tabcontent, tablinks;

   tabcontent = document.getElementsByClassName("tabcontent");
   for(i = 0; i < tabcontent.length; i++){
      tabcontent[i].style.display = "none";
   }
   tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
   document.getElementById(name).style.display = "block";
   opt.currentTarget.className += " active";
}
