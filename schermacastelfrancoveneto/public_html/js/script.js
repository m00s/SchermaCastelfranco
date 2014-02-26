/* SCRIPT PER LA GESTIONE RESPONSIVE DEL MENU' E DEI LINK ESTERNI*/

$(document).ready(function(){

	$("#sezione-nav-1").click(function(){
		var presente=$("#panel-nav-1").css("display");
		if (presente=="none"){
			$("#panel-nav-1").css("display","block");
		}else{
			$("#panel-nav-1").css("display","");
		}

	});
});

$(document).ready(function(){

	$("#sezione-sidebar").click(function(){
		var presente=$("#panel-sidebar").css("display");
		if (presente=="none"){
			$("#panel-sidebar").css("display","block");
		}else{
			$("#panel-sidebar").css("display","");
		}

	});
});

$(document).ready(function(){

	$(".sezione").click(function(){
		var presente=$(".nascondi-articolo").css("display");
		if (presente=="none"){
			$(".nascondi-articolo").css("display","block");
		}else{
			$(".nascondi-articolo").css("display","");
		}

	});
});


/* FINE */

/* SCRIPT PER LA GESTIONE DELL'EDITOR DELL'AREA RISERVATA */




/* FINE */

/* SCRIPT PER LO SFONDO DELLA HOME */
$(document).ready(function(){
    $("#sfondo").fadeIn(5000);
});
/* FINE */