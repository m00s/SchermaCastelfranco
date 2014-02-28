<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:s="http://www.schermacastelfranco.com" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>

<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="it">
<head>
	<title>Articoli - Scherma Castelfranco Veneto </title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<meta name="title" content="Scherma Castelfranco - Articoli" />
	<link href="stile.css" rel="stylesheet" type="text/css" media="screen"/>
	<link href="print.css" rel="stylesheet" type="text/css" media="print"/>
</head>

<body>
	<div id="header">
	</div>
	<div id="nav">
		<div id="nav-1">
			<ul id="sezione-nav-1"><li id="image-menu" title="contiene immagine del menù per il mobile"></li></ul>
			<ul id="panel-nav-1">
				<li><a href="#">Articoli</a></li>
				<li><a href="#">Documenti</a></li>
				<li><a href="../cgi-bin/prova_perl.cgi">Storia</a></li>
				<li><a href="#">Staff</a></li>
				<li id="last-link"><a href="#">Corsi</a></li>
			</ul>
		</div>
		<div id="nav-2">
			<a href="#">Accedi Area Riservata</a>
			<span>RICERCA [-----------]</span>
		</div>
	</div>
	<div id="breadcrumb">
			<p>Ti trovi in: Articoli</p>
		</div>

		<div id="content">
			<xsl:for-each select="testi/articolo">
				<div class="article">
					<div class="sezione">
						<p><xsl:value-of select="data"/></p>
						<p><xsl:value-of select="luogo"/></p>
						<h1><xsl:value-of select="titolo"/></h1>
					</div>
					<div class="nascondi-articolo">
						<xsl:copy-of select="img">
						<p class="nascondi-articolo">
							<xsl:value-of select="paragrafo"/>
						</p>
						<p><a href="#content">Torna su</a></p>
					</div>
				</div>
			</xsl:for-each>
		</div>
</body>

</xsl:template>
</xsl:stylesheet>