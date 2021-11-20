$(function() {
    $(".question").each(function() {
        // Ajouter le bouton vrai
        $("<button>")
            .addClass("btn btn-success")
            .text("Vrai")
            .css("margin-right", "15px")
            .appendTo(this);
        // Ajouter le bouton faux
        $("<button>")
            .addClass("btn btn-danger")
            .text("Faux")
            .css("margin-right", "15px")
            .appendTo(this);
    });
    $(".question button").click(function() {
        //Contrôler s'il y a correspondance entre le bouton cliquer (vrai/faux) et le type de question (question-true/question-false)
        if (($(this).text() == "Vrai" & $(this).parent().hasClass("question-true")) || ($(this).text() == "Faux" & $(this).parent().hasClass("question-false"))) {
            $('<label>').addClass('text-success').text('Correct !').appendTo($(this).parent());
        } else {
            $('<label>').addClass('text-danger').text('Erreur !').appendTo($(this).parent());
        }
        //désactiver l'autre bouton de la question
        $(this).siblings("button").attr("disabled", "disabled");
    });

});
$(function() {
    $(".cloche").mouseenter(function() {
        $(".cloche").animate({
            left: '200px'
        });
    });
    $(".cloche").click(function() {
        $(".modal").show(1000);
    });
    $(".btn-danger").click(function() {
        $(".modal").hide(1000);
    });
    $(".carte").mouseenter(function() {
        $(this).animate({
            left: '200px',
            height: '500px',
            width: '500px'
        });
    });
});