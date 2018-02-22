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

function logIn(){
   var usr = document.getElementById("userIn").value;
   var pass = document.getElementById("passwordDoctor").value;
   if (usr == "doctor" && pass == "a"){
      return true;
   }
   else{
      alert("Login Invalid - Try again.");
   }
   return false;
}
/*function loginRedirect(){
   var done = 0;
   var username = document.getElementById("userLogIn").value;
   var password = document.getElementByI("passwordLogIn").value;
   if(username == "doctor" && password == "a"){ window.location.replace("newExist.html");}
   else {alert("Login Invalid - Try again.");}
   return false;
}*/


/*
function validateForm() {
        var un = document.loginform.usr.value;
        var pw = document.loginform.pword.value;
        var name = "username";
        var word = "password";
        if ((un == "doctor") && (pw == "a")) {
            window.location("newExist.html");
        }
        else {
            alert ("Login was unsuccessful, please check your username and password");

        }
  }*/
  function check(form)
  {

   if(form.userid.value == "doctor" && form.pswrd.value == "a")
    {
      window.open('file:///home/david/3rdYearProject/UI/newExist.html')
    }
   else
   {
     alert("Please subscribe to my channel for more coding!")
    }
  }
