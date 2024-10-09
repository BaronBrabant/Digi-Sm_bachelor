function checklistPopup(id) {
    var popup = document.getElementById(id);
    console.log(popup)
    popup.classList.toggle("show");
  }

function helperButton(id){
var popup = document.getElementById(id);
console.log(popup)
popup.classList.toggle("show");
}


function modify_value(id) {
if (id == 'username'){
    val = prompt("Please enter your new username");
    return window.location = "/modify_username/" + val;
}else if (id == 'name'){
    val = prompt("Please enter your new name");
    return window.location = "/modify_name/" + val;
}else if (id == 'firstname'){
    val = prompt("Please enter your new firstname");
    return window.location = "/modify_firstname/" + val;
}
}


function styleRowSprintCreation(row) { 
    //console.log(row);   
    row.style.backgroundColor = 'RGB(255, 245, 175)';
}

function addToSprint(elem) {
    let id = elem;

    let taskExists = sessionStorage.getItem(id);

    if (taskExists == null) {
        sessionStorage.setItem(id, JSON.stringify(id));

        //console.log(sessionStorage.getItem(id)==sessionStorage.key(0));
    } else {
        //console.log(sessionStorage.getItem(id));
        //console.log(Number.isInteger(parseInt(sessionStorage.getItem(id))));
       
        if (Number.isInteger(parseInt(sessionStorage.getItem(id)))) {
            
            //console.log(sessionStorage.getItem(id));
            
            document.getElementById(sessionStorage.getItem(id)).style.backgroundColor = 'rgb(255, 255, 255)';
            //document.getElementById(sessionStorage.getItem(id)).style.color = 'white';

            sessionStorage.removeItem(id);
        }
    }


    //console.log(sessionStorage.length);

    var table = document.getElementById("tableUS");

    for (var i = 1, row; row = table.rows[i]; i++) {
      
        if (document.getElementById(sessionStorage.getItem(row.id)) != null){
            styleRowSprintCreation(document.getElementById(sessionStorage.getItem(row.id)))
            //console.log(sessionStorage.getItem(sessionStorage.key(i)));
        }
    }

    /*
    for (let i = 0; i < sessionStorage.length; i++) {
        //console.log(i)
        //console.log(sessionStorage.key(i));
        //console.log(document.getElementById(sessionStorage.key(i)));
        
        if (document.getElementById(sessionStorage.key(i)) != null){
        styleRowSprintCreation(document.getElementById(sessionStorage.key(i)))
        //console.log(sessionStorage.getItem(sessionStorage.key(i)));
        }
    }
    */
    //styleBasketButton(elem);
}


function sendListBackend() {

    let userS = Object.keys(sessionStorage);

    console.log(userS.length);
    if (userS.length == 0){
        alert("You need to select at least one user story to create a sprint");
        return;
    }
    else {
    jQuery.ajax({
        type : 'POST',
        data : {'data':JSON.stringify(userS)},
        url : "/create_sprint",
        success: function () {
            sessionStorage.clear();
            location.href = '/';
        }
      });
    
    }
}


function ownAdminDemotionAlert() {
    alert("You can't demote yourself! Enjoy the admin rights while you can!");
}

function ownBlockAlert() {
    alert("You can't block yourself!");
}



//drag and drop functionallity on user story list of sprint


var row;
let validLastRowId;

function start(){

  row = event.target;
}
function dragover(){
  
  var e = event;
  e.preventDefault();

  let children= Array.from(e.target.parentNode.parentNode.children);
  
  if (children.indexOf(row) != -1){
    validLastRowId = children.indexOf(row);
    console.log(row.id);
    console.log(validLastRowId);
    if(children.indexOf(e.target.parentNode)>children.indexOf(row)){
        e.target.parentNode.after(row);
        //console.log(validLastRowId);
    }else
        e.target.parentNode.before(row);
        //console.log(validLastRowId);

  }


}

function sendNewOrderBackend() {

    //This function is called when the user clicks on any buttons going away from the 
    //home page, when that happens the order of the user stories is sent to the backend
    var table = document.getElementById("table countable");
    var newOrder = [];

    sessionStorage.clear();

    for (var i = 0, row; row = table.rows[i]; i++) {
        //iterate through rows
        //rows would be accessed using the "row" variable assigned in the for loop
        newOrder[i] = row.id;

    }
    
    jQuery.ajax({
        type : 'POST',
        data : {'data':JSON.stringify(newOrder)},
        url : "/update_order"
      });
}

function sendNewOrderBackendHomePage() {

    //This function is called when the user clicks on any buttons going away from the 
    //home page, when that happens the order of the user stories is sent to the backend
    //The difference to the function above is that if the user clicks on the home button
    //the route made to update the order is works but by the time it updates the database
    //the home page has already loaded the old order. So the state of the database and the
    //front end is staggered and keeps alternating between the two orders. This function
    //sends the changes straight the the "/" route preventing the problem above.

    var table = document.getElementById("table countable");
    var newOrder = [];

    sessionStorage.clear();

    if (table != null){
        for (var i = 0, row; row = table.rows[i]; i++) {
            //iterate through rows
            //rows would be accessed using the "row" variable assigned in the for loop
            newOrder[i] = row.id;

        }
    }
    else{
        newOrder[0] = "empty";
    }

    console.log(newOrder)

    jQuery.ajax({
        type : 'POST',
        data : {'data':JSON.stringify(newOrder)},
        url : "/",
        });
}

function inviteFriendButton(id) {

    let userS = id;
    
    jQuery.ajax({
        type : 'POST',
        data : {'data':JSON.stringify(userS)},
        url : "/addUserProjectButton",
        success: function () {
            location.href = '/friends';
        }
      });

}

function loadSprints(id, stepDirection) {

    let sprintMultiple = [id, stepDirection];
    
    jQuery.ajax({
        type : 'POST',
        data : {'step':JSON.stringify(sprintMultiple)},
        url : "/",
        success: function () {
            location.href = '/';
        }
      });

}




