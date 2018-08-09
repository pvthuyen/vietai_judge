/* Update API endpoint */

var LOGIN_API = "/user/login";
var UPLOAD_API = "/judge/upload";

var user_name = "BaoTran";
var display_user_name = "Bao Tran";
var homework_name = "Sample Tutorial";
var exercisesID = "";

var list_exercises = [
  { name: "Bai tap 1", id: "bt1", "status": "None"},
  { name: "Bai tap 2", id: "bt2", "status": "None"},
];

function submitLogin() {
  var user_name = document.getElementById("uname").value;
  var psw = document.getElementById("psw").value;
  /********** LOGIN_API ********
    Input:
      - user_name
      - password
    Return:
      - success                     true/false
      - display_user_name           name to display
      - homework_name               name of current homework (tutorial/assigment name)
      - list_exercises              list of exercises { name:     name of excersise (ex1, ex2, ect.),
                                                        id  :     exercise's ID
                                                        status:   "None"(if haven't submitted)/ Score/ "Runtime Error" }
  *******************************/
  var data = {user_name: user_name, password: psw};
  $.post(LOGIN_API, data, function(result){
      if (result["success"] == true){
        display_user_name = result.display_user_name;
        homework_name = result.homework_name;
        list_exercises = result.list_exercises;

        $("#vietai-name").html(display_user_name);
        $("#vietai-homework-name").html(homework_name);
        $("#vietai-login-form").hide();
        $("#vietai-welcome").css("display", "block");
        $("#vietai-homework").css("display", "flex");
        renderHomework();
      } else {
        alert("Login Error! Please check your username & password, or contact Teaching Team!")
      }
  }).fail(function(response) {
    alert("Server issue! Please contact Teaching Team")
  });

  // Test data
  // $("#vietai-name").html(user_name);
  // $("#vietai-homework-name").html(homework_name);
  // $("#vietai-login-form").hide();
  // $("#vietai-welcome").css("display", "block");
  // $("#vietai-homework").css("display", "flex");
  //
  // renderHomework();
}

function uploadFile(e){
  var file = e.target.result;
   if (file && file.length) {
       /********** UPLOAD_API ********
         Input:
           - user_name
           - exercisesID
           - file_content (string)
         Output:
           - success    true/false
           - status     "None"(if haven't submitted)/ Score/ "Runtime Error"
       *******************************/
       data = {
         user: user_name,
         ex_name: exercisesID,
         file_content: file
       };
       $.post(UPLOAD_API, data, function(result){
         if (result["success"] == true){
           $("#status_" + exercisesID).html(result["status"]);
         } else {
           alert("Login Error! Please contact Teaching Team!")
         }
       }).fail(function(response) {
         alert("Server issue! Please contact Teaching Team")
       });

       // Test data
       // $("#status_" + exercisesID).html("Runtime Error");
   }
}



function renderHomework() {
  $("#vietai-ex-name").html();
  $("#vietai-homework-submit").html();
  $("#vietai-homework-status").html();

  var homework_name_html = "";
  var homework_submit_html = "";
  var homework_status_html = "";

  for (var i = 0; i<= list_exercises.length - 1; i++) {
    homework_name_html += '<li class="list-group-item vietai-cell">' + list_exercises[i].name +'</li>';
    homework_submit_html += '<li class="list-group-item vietai-cell vietai-overflow">' +
                              '<form>' +
                                '<div class="form-group">' +
                                  '<div class="row">' +
                                    '<div class="col-md-9 vietai-overflow">' +
                                      '<input type="file" class="form-control-file" id=' + list_exercises[i].id +'>' +
                                    '</div>' +
                                    '<div class="col-md-3">' +
                                      '<button type="button" class="btn btn-info" onClick=submitExercises("'+ list_exercises[i].id +'") >Submit</button>' +
                                    '</div>' +
                                  '</div>' +
                                '</div>' +
                              '</form>' +
                            '</li>';
    homework_status_html += '<li class="list-group-item vietai-cell" id="status_' + list_exercises[i].id +'">' +list_exercises[i].status +'</li>';
  }

  $("#vietai-ex-name").html(homework_name_html);
  $("#vietai-homework-submit").html(homework_submit_html);
  $("#vietai-homework-status").html(homework_status_html);
}


function submitExercises(exID) {
  exercisesID = exID;
  var files = document.getElementById(exercisesID).files;
  if (!files.length) {
    alert('Please select a file!');
    return;
  }
  var file = files[0];
  if (file.type.localeCompare("text/plain")!==0) {
    alert('Please upload a text file!');
    return;
  }

  var spin = '<i class="fa fa-spinner fa-spin" style="font-size:24px"></i>';
  $("#status_" + exercisesID).html(spin);

  var reader = new FileReader();
  reader.readAsText(file);
  $(reader).on('load', uploadFile);

}