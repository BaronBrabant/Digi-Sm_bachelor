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
    //console.log(id);

    let taskExists = sessionStorage.getItem(id);
    

    if (taskExists == null) {
        sessionStorage.setItem(id, JSON.stringify(id));
        //console.log(sessionStorage.getItem(id)==sessionStorage.key(0));
    } else {
        console.log(sessionStorage.getItem(id));
        console.log(Number.isInteger(parseInt(sessionStorage.getItem(id))));
       
        if (Number.isInteger(parseInt(sessionStorage.getItem(id)))) {
            
            //console.log(sessionStorage.key(id));
        
            document.getElementById(sessionStorage.getItem(id)).style.backgroundColor = 'rgb(255, 255, 255)';
            //document.getElementById(sessionStorage.getItem(id)).style.color = 'white';

            sessionStorage.removeItem(id);
        }
    }


    //console.log(sessionStorage.getItem(id));

    for (let i = 0; i < sessionStorage.length; i++) {
        //console.log(i)
        //console.log(sessionStorage.key(i));
        styleRowSprintCreation(document.getElementById(sessionStorage.key(i)))
        //console.log(sessionStorage.getItem(sessionStorage.key(i)));

    }
    //styleBasketButton(elem);
}


function sendListBackend() {

    let userS = Object.keys(sessionStorage);
    
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



jQuery(document).ready(function() {
    $("#pieChartButton").click(function(){
        $("#pieChart").css("display", "show");
        $("#burnDownChart").css("display", "none");

        
    });
});

jQuery(document).ready(function() {
    $("#burnDownChartButton").click(function(){
        $("#burnDownChart").css("display", "show");
        $("#pieChart").css("display", "none");
    });
});





//jQuery(document).ready(function($) {
//    $(".clickable-row").click(function() {
//        window.location = $(this).data("href");
//    });
//});


