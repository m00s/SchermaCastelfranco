<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:s="http://www.schermacastelfranco.com" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>

<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<title>Documenti - Scherma Castelfranco Veneto </title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<meta name="title" content="Scherma Castelfranco - Articoli" />
	<meta name="description" content="(Quasi) tutti i personaggi di Angry Birds" />
	<meta name="keywords" content="scherma, spada" />
	<meta name="language" content="italian it" />
	<meta name="author" content="L'intrusa" />
	<link href="../public_html/css/stile.css" rel="stylesheet" type="text/css" media="screen"/>
	<link href="../public_html/css/print.css" rel="stylesheet" type="text/css" media="print"/>
</head>

<body>
	<div id="header">
	</div>
	<div id="nav">
		<div id="nav-1">
			<ul id="sezione-nav-1"><li id="image-menu" title="contiene immagine del menù per il mobile"></li></ul>
			<ul id="panel-nav-1">
				<li><a href="#">Articoli</a></li>
				<li>Documenti</li>
				<li><a href="../cgi-bin/prova_perl.cgi">Storia</a></li>
				<li><a href="#">Staff</a></li>
				<li id="last-link"><a href="#">Corsi</a></li>
			</ul>
		</div>
		<div id="nav-2">
			<a href="#">Area Riservata</a>
		</div>
	</div>
	<div id="breadcrumb">
		<p>Ti trovi in: Documenti</p>
	</div>

	<div id="content">
		<xsl:for-each select="a:testi/a:documento">
			<div class="document">
				
			</div>
		</xsl:for-each>
	</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>