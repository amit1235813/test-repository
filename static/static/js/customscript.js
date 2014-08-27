// Fading out the exam list and fading in the activity list

function loadActivity(){
    $(document).ready(function(){
      $("#exam").find(".btn-group").click(function(){
        $("#exam").fadeOut("slow", function(){
        $("#activity").fadeIn("slow");
        });
      });
    });
}

// Moving to the second page - 24 of them - 3 templates

function loadPracticepage(){
    $(document).ready(function(){
      $("#class12").click(function(){
          $("#practice").click(function(){
            $("#activity").fadeOut("slow", function(){
            window.open("/page2_1/", "_self");
            });
          });
      });
    });
}
