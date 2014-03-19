
/* Script di controllo preventivo dei campi del login */

function checkLogin(){
		var username = document.loginForm.username.value;
		var password = document.loginForm.password.value;
		var uok=true;
		var pok=true;

		if ((username == "") || (username == "undefined")){
			document.getElementById('userError').innerHTML = '(!) Username non valido';
			uok=false;
		}
		else{
			document.getElementById('userError').innerHTML = '';
			uok=true;
		}
		if ((password == "") || (password == "undefined")){
			document.getElementById('passError').innerHTML = '(!) Password non valida';
			pok=false;
		}
		else{
			document.getElementById('passError').innerHTML = '';
			pok=true;
		}

		return (uok && pok);
	}
/* FINE */

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

/* SCRIPT PER LA GESTIONE RESPONSIVE DEL MENU', DEI LINK ESTERNI E DEI DOCUMENTI/ARTICOLI */

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

/* SCRIPT PER LA PREVALIDAZIONE DEI FORM DI INSERIMENTO */

function checkInserimentoArticolo(){
	var luogo = document.inserisciArticoloForm.luogo.value;
	var datepicker = document.inserisciArticoloForm.datepicker.value;
	var titolo = document.inserisciArticoloForm.titolo.value;
	var testo = document.inserisciArticoloForm.testo.value;
	var altfoto = document.inserisciArticoloForm.altfoto.value;
	var lok = true;
	var dok = true;
	var tok = true;
	var teok = true;
	var aok = true;

	document.getElementById('errors').innerHTML = " ";

	if ((luogo == "") || (luogo == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Luogo non valido';
			lok=false;
		}

	if ((datepicker == "") || (datepicker == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Data non valida';
			dok=false;
		}

	if ((titolo == "") || (titolo == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Titolo non valido';
			tok=false;
		}

	if ((testo == "") || (testo == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Testo non valido';
			teok=false;
		}

	if ((altfoto == "") || (altfoto == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Descrizione fotografia non valida';
			aok=false;
		}

	return (lok && dok && tok && teok && aok);
}

function checkInserimentoDocumento(){
	var titolo = document.inserisciDocumentoForm.titolo.value;
	var testo = document.inserisciDocumentoForm.testo.value;
	var tok = true;
	var teok = true;

	document.getElementById('errors').innerHTML = " ";

	if ((titolo == "") || (titolo == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Titolo non valido';
			tok=false;
		}

	if ((testo == "") || (testo == "undefined")){
			document.getElementById('errors').innerHTML += '<br /> (!) Testo non valido';
			teok=false;
		}

	return (tok && teok);
}

/* FINE */


/* CAMBIO DI SELECT VALUE*/

function selectChange(){
	document.selectCategory.submit();
}

/* FINE */

/* SCRIPT RIPOSIZIONAMENTO ULTIMI ARTICOLI VISUALIZZATI */

function scrollTo(){
	location.hash = "#anchor";
}

/* FINE */


/* SCRIPT PER LA GESTIONE DELL'EDITOR DELL'AREA RISERVATA */

		var idTextArea;

		function setId(idValue){
			idTextArea=idValue;
		}

		$(document).ready(function () {
            $("#testo").change(
                function () {
					var text = document.getElementById("testo").value;
					document.getElementById("trasfTesto").innerHTML = text;
                }
            );


            $("#datepicker").change(
                function () {
                	var date = document.getElementById("datepicker").value;
					document.getElementById("trasfData").innerHTML = date;
				}
            );

            $("#titolo").change(
                function () {
                	var title = document.getElementById("titolo").value;
					document.getElementById("trasfTitolo").innerHTML = title;
				}
            );


        });

			function InsertCodeInTextArea(textValue) {
		        //Get textArea HTML control
		        var txtArea = document.getElementById(idTextArea);

		        //IE
		        if (document.selection) {
		            txtArea.focus();
		            var sel = document.selection.createRange();
		            sel.text = textValue;
		            return;
		        }
		        //Firefox, chrome, mozilla
		        else if (txtArea.selectionStart || txtArea.selectionStart == '0') {
		            var startPos = txtArea.selectionStart;
		            var endPos = txtArea.selectionEnd;
		            var scrollTop = txtArea.scrollTop;
		            txtArea.value = txtArea.value.substring(0, startPos) + textValue + txtArea.value.substring(endPos, txtArea.value.length);
		            txtArea.focus();
		            txtArea.selectionStart = startPos + textValue.length;
		            txtArea.selectionEnd = startPos + textValue.length;
		        }
		        else {
		            txtArea.value += textArea.value;
		            txtArea.focus();
		        }
		    }

			$(function() {
				$("#datepicker").datepicker({
					dateFormat: "dd/mm/yy",
					onSelect: function(dateText, inst) {
						var date = $.datepicker.parseDate(inst.settings.dateFormat || $.datepicker._defaults.dateFormat, dateText, inst.settings);
						var dateText1 = $.datepicker.formatDate("D, d M yy", date, inst.settings);
						date.setDate(date.getDate() + 7);
						var dateText2 = $.datepicker.formatDate("D, d M yy", date, inst.settings);
					}
				});
			});

/* FINE */


/* SCRIPT PER IL BOX TORNA SU */

$(function() {
	  $(window).scroll(function() {
	       if($(this).scrollTop() > 0) {
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

/* FINE */

/* GESTIONE SIDEBAR POSIZIONAMENTO*/
/*
$(document).ready(function(){
	var topFixed=272;

	var msie6 = $.browser == 'msie' && $.browser.version < 7;
	// var safari = ;
	if ($(window).width()>850){
		if (!msie6){
			// alert(topFixed);
			var top=$("#sidebar").offset().top - parseFloat($("#sidebar").css("marginTop").replace(/auto/,0));
			// alert(top);
			var y=$(window).scrollTop();
			// alert(y);

			if (y>=top){
				$("#sidebar").addClass("sidebar-fixed");
				$("#sidebar").css("margin-top","0");
				$("#sidebar").css("width","21.6%");
			}
			$(window).scroll(function(){
				var y=$(window).scrollTop();
				if (y>= top){
					$("#sidebar").addClass("sidebar-fixed");
					$("#sidebar").css("margin-top","0");
					$("#sidebar").css("width","21.6%");
				}else{
					$("#sidebar").removeClass("sidebar-fixed");
					$("#sidebar").css("margin-top","3%");
					$("#sidebar").css("width","23%");
				}
				/*
				if ($(window).width()<850){
						$("#sidebar").removeClass("sidebar-fixed")
						$("#sidebar").css("width","99%");
						$("#sidebar").css("margin-top","0");
				}
				*/
//			});

//	}
//	}

//});


/*
function staticF(){
	$("#sidebar").css({
		"position": "static",
		"display": "block",
		"float": "left",
		"clear": "both",
		"margin-top": "0",
		"width": "99%"

	});
}

/*

/* FINE */