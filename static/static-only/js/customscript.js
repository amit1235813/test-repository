// Fading out the exam list

function loadActivity(){
  $("#exam .btn-group").click(function(){
    $("#exam").fadeOut("slow", function(){
    $("#activity").fadeIn("slow");
    });
  });
}

// Moving to the second page - 24 of them

function loadSecondpage(){
  $(("#exam #class12") && ("#activity #practice")).click(function(){
    $("#activity").fadeOut("slow", function(){
    window.open("http://localhost/bootstrap//page2_class12_practice_questions.html", "_self");
    });
  });
}
