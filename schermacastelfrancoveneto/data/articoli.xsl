<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:a="http://www.articoli.com" exclude-result-prefixes="a">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Articoli - Scherma Castelfranco Veneto</title>
		<meta name="description" content="Pagina che mostra gli articoli delle gare disputate dal Circolo di Scherma di Castefranco Veneto redatti dal presidente dell'associazione" />
		<meta name="author" content="Chiara Bigarella, Mirko Pavanello, Massimiliano Sartoretto, Paolo Tesser" />
		<meta name="keywords" content="circolo, scherma, articoli, news, notizie, Castelfranco Veneto" />
		<meta name="robots" content="index,follow" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="stylesheet" href="../public_html/css/stile.css" type="text/css"/>
		<link rel="stylesheet" href="../public_html/css/screen.css" type="text/css" media="screen" />
		<link rel="stylesheet" href="../public_html/css/print.css" type="text/css" media="print" />
		<link rel="Shortcut Icon" href="../public_html/img/struttura/favicon.ico" type="image/x-icon" />
		<script  type="text/javascript" charset="UTF-8" src="../public_html/js/jquery.js" ></script>
		<script  type="text/javascript" charset="UTF-8" src="../public_html/js/script.js" ></script>
	</head>
	<body>
		<div id="header">

		</div>

		<div id="nav">
			<a href="#content" class="nascondi">Salta <span xml:lang="fr">menù</span> contenente anche il <span xml:lang="en">link</span> per l'accesso all'area riservata</a>
			<div id="nav-1">
				<ul id="sezione-nav-1"><li id="image-menu" title="contiene immagine del menù per il mobile"></li></ul>
				<ul id="panel-nav-1">
					<li id="active" >ARTICOLO</li>
					<li><a href="documenti.xml" tabindex="1">DOCUMENTI</a></li>
					<li><a href="../public_html/storia.html" tabindex="2">STORIA</a></li>
					<li><a href="../public_html/staff.html" tabindex="3"><span xml:lang="en">STAFF</span></a></li>
					<li class="last-link"><a href="../public_html/corsi.html" tabindex="4">CORSI</a></li>
				</ul>
			</div>
			<div id="nav-2">
				<a href="#" tabindex="5">Area Riservata</a>
				<a href="../public_html/mappa.html" tabindex="6">Mappa del sito</a>
			</div>

		</div>

		<div id="breadcrumb">
			<p>Ti trovi in: <span xml:lang="en">Articoli</span></p>
		</div>
		<a href="#sidebar" class="nascondi">Salta contenuto e vai alla <span xml:lang="en">sidebar</span> contenente <span xml:lang="en">link</span> ad altri siti di scherma e agli <span xml:lang="en">sponsor</span></a>

		<!--  INIZIO SEZIONE "XSL" DA SISTEMARE -->
		<div id="content">
			<xsl:for-each select="a:testi/a:articolo">

				<div class="article">
					<div class="sezione">
						<p><xsl:value-of select="a:data"/></p>
						<p><xsl:value-of select="a:luogo"/></p>
						<h1><xsl:value-of select="a:titolo"/></h1>
					</div>
					<div class="nascondi-articolo">
						<xsl:copy-of select="a:img"/>
						<p class="nascondi-articolo">
							<xsl:value-of select="a:paragrafo"/>
						</p>
						<p class="nascondi"><a href="#content">Torna sù al contenuto della pagina</a>o <a href="#nav">torna al <span xml:lang="fr">menù</span> di navigazione</a></p>
					</div>
					<p><a href="#">Vai all'articolo intero</a></p>
				</div>

			</xsl:for-each>
		</div>
		<!--  FINE SEZIONE -->

		<div id="sidebar">
			<div id="sezione-sidebar"><p><span xml:lang="en">LINK</span> ESTERNI</p></div>
			<div id="panel-sidebar">
				<ul title="lista contenente dei link riferenti agli sponsor del circolo">
					<li><span xml:lang="en" class="desc-li">SPONSOR LINK</span>
						<ul>
							<li title="link che manda al sito della Fabbian, sponsor del circolo"><a href="http://www.fabbian.com/it" target="_blank">Fabbian</a></li>
							<li title="link che manda al sito della Goppion Caffè, sponsor del circolo"><a href="http://www.goppioncaffe.it" target="_blank">Goppion</a></li>
							<li title="link che manda al sito del Carminari, sponsor del circolo"><a href="http://www.carmimari.com" target="_blank">Carminari</a></li>
							<li title="link che manda al sito della Gnocchi Master, sponsor del circolo"><a href="http://www.gnocchimaster.com" target="_blank">Gnocchi <span xml:lang="en">Master</span></a></li>
						</ul>
					</li>
				</ul>
				<ul title="lista contenente dei link riferenti ad altri siti di scherma">
					<li><span xml:lang="en" class="desc-li">SCHERMA LINK</span>
						<ul>
							<li title="link che manda al sito della federazione internazionale di scherma"><a href="http://www.fie.ch" target="_blank"><abbr title="Federazione Internazionale Scherma">FIE</abbr></a></li>
							<li title="link che manda al sito della federazione italiana di scherma"><a href="http://www.federscherma.it/index.asp" target="_blank"><span xml:lang="en">Federal Scherma</span></a></li>
							<li title="link che manda al sito della federazione veneta di scherma"><a href="http://www.schermaveneto.it" target="_blank">Scherma Veneto</a></li>
							<li title="link che manda al sito del comune di Castelfranco Veneto"><a href="http://www.comune.castelfrancoveneto.tv.it" target="_blank">Comune Castelfranco Veneto</a></li>
						</ul>
					</li>
				</ul>

				<ul><li title="link che manda alla pagina Google Foto contenente tutte le immagine delle gare disputate dal circolo"><a href="https://plus.google.com/photos/100772179390595520915/albums?banner=pwa" target="_blank"><span xml:lang="en" class="desc-li">GALLERY</span></a></li></ul>
			</div>
		</div>


		<div id="footer">
			<img class="footerElement" src="../public_html/img/struttura/valid-xhtml11.png" alt=""/>
			<span xml:lang="en" class="footerElement"> - All rights reserved - </span>
			<img class="footerElement" src="../public_html/img/struttura/vcss-blue.gif" alt=""/>
		</div>


</body>
</html>
</xsl:template>
</xsl:stylesheet>