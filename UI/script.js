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
