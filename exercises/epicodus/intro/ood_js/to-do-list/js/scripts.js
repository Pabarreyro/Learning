// business logic

function Task(name, dueDate, details) {
  this.name = name;
  this.dueDate = dueDate;
  this.details = details;
};


//user logic
$(function(){
  $("#form-one").submit(function(event) {
    event.preventDefault();

    let inputName = $("#input-name").val();
    let inputDueDate = $("#input-duedate").val();
    let inputDetails = $("#input-details").val();

    let newTask = new Task(inputName, inputDueDate, inputDetails);

    $("ul#todolist").append("<li><span class='task'>" +newTask.name+ "</span></li>")

    

  });


});
