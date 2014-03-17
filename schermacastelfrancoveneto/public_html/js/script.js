
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
/* SCRIPT PER LA GESTIONE RESPONSIVE DEL MENU' E DEI LINK ESTERNI */

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
		/* $(this).hide(); */
		var id=$(this).attr('id'); // mi salvo l'id dell'articolo su cui clicco
		var parent = $(this).parent("div"); // .attr('id'); // closest // risalgo al padre dell'elemento su cui abbiamo fatto il click
		var son = parent.find(".nascondi-articolo");

		var attr = son.attr('id');
		// alert(attr);

		if (attr === undefined) {
			son.attr('id','mostra');
		}else{
			// alert('attributo esiste');
			son.removeAttr("id");
		}

		var attr = son.attr('id');
		// alert(attr);

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


	$(function() {
	    $(window).scroll(function() {
	        if($(this).scrollTop() > 300) {
	                        //se non siamo in cima alla pagina
	            $('#boxTop').fadeIn(); //faccio apparire il box    
	        } else {
	                        //altrimenti (il visitatore è in cima alla pagina scrollTop = 0)
	            $('#boxTop').fadeOut();//Il box scompare
	        }
	    });//Allo scroll function
	 
	    $('#boxTop').click(function() {
	                //Se clicco sul box torno su (scrollTop:0) con un timing di animazione.
	        $('body,html').animate({scrollTop:0},800);
	    });//Click
	 
	});//DOM