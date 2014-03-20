sub articoloCompleto() {

my $file="../data/articoli.xml";

# creazione PARSER
my $parser=XML::LibXML->new();
# apertura file e lettura input
my $doc=$parser->parse_file($file); # da testo a struttura ad albero

my $data="d";
my $luogo="l";

#recupero parametri formali
if ($_[0] && $_[1]) {
	$data=$_[0];
	$luogo=$_[1];
	$luogo=~ s/%20/ /;
}

my $paragrafo="p";
my $titolo="t";
my $img="i";

my $artNodo=$doc->findnodes("//ts:articolo[ts:data='$data' and ts:luogo='$luogo']")->get_node(1);

#estrazione IMMAGINE con attributi
my $imgNodo=$doc->findnodes("//ts:articolo[ts:data='$data' and ts:luogo='$luogo']/ts:img")->get_node(1);
my @imgAtts = $imgNodo->getAttributes();
my %imgAttsString;
foreach $imgAtt (@imgAtts) {
	my $nome_a = $imgAtt->getName();
	my $valore_a = $imgAtt->getValue();
	$imgAttsString{$nome_a}=$nome_a."=\"".$valore_a."\"";
}
my $src=$imgAttsString{'src'};
my $alt=$imgAttsString{'alt'};
$img="<img ".$src." ".$alt." />";

#estrazione PARAGRAFO con nodi figli:
my $parNodo=$artNodo->getElementsByTagName("paragrafo");

$paragrafo=$parNodo->item(0)->toString;
$paragrafo=~ s/\<paragrafo\>//;
$paragrafo=~ s/\<\/paragrafo\>//;

#estrazione TITOLO con nodi figli:
my $titoloNodo=$artNodo->getElementsByTagName("titolo");

$titolo=$titoloNodo->item(0)->toString;
$titolo=~ s/\<titolo\>//;
$titolo=~ s/\<\/titolo\>//;



#STAMPA PAGINA HTML: (controllare link)
print "Content-type: text/html\n\n";
print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" version="-//W3C//DTD XHTML 1.1//EN" xml:lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Articolo completo  - Scherma Castelfranco Veneto</title>
		<meta name="description" content="Pagina che visualizza un articolo completo" />
		<meta name="author" content="Chiara Bigarella, Mirko Pavanello, Massimiliano Sartoretto, Paolo Tesser" />
		<meta name="robots" content="index, follow" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="stylesheet" href="../css/stile.css" type="text/css"/>
		<link rel="stylesheet" href="../css/print.css" type="text/css" media="print" />
		<link rel="Shortcut Icon" href="../img/struttura/favicon.ico" type="image/x-icon" />
		<link href="../css/ui-lightness/jquery-ui-1.10.4.custom.css" rel="stylesheet"/>
		<link type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/themes/ui-darkness/jquery-ui.css" rel="stylesheet"/>
		<script type="text/javascript" src="../js/librerie/jquery-ui-1.10.4.custom.min.js"></script>
		<script  type="text/javascript" charset="UTF-8" src="../js/librerie/jquery-1.11.0.min.js" ></script>
		<script  type="text/javascript" charset="UTF-8" src="../js/script.js" ></script>
		<noscript>
			<link rel="stylesheet" href="../css/stilenojava.css" type="text/css"/>
		</noscript>
	</head>

	<body>
		<div id="header">
		</div>

		<a href="#breadcrumb" class="nascondi">Salta <span xml:lang="fr">menù</span> contenente anche il <span xml:lang="en">link</span> per l'accesso all'area riservata</a>

		<div id="nav">
			<div id="nav-1">
				<ul id="sezione-nav-1"><li id="image-menu" title="contiene immagine del menù per il mobile"></li></ul>
				<ul id="panel-nav-1">
					<li id="active" >ARTICOLO</li>
					<li><a href="documenti.cgi" tabindex="1">DOCUMENTI</a></li>
					<li><a href="../storia.html" tabindex="2">STORIA</a></li>
					<li><a href="../staff.html" tabindex="3"><span xml:lang="en">STAFF</span></a></li>
					<li class="last-link"><a href="../corsi.html" tabindex="4">CORSI</a></li>
				</ul>
			</div>
			<div id="nav-2">
				<a href="../login.html" tabindex="5">Area Riservata</a>
				<a href="../mappa.html" tabindex="6">Mappa del sito</a>
			</div>

		</div>

		<div id="breadcrumb">
			<p>Ti trovi in: Articoli</p>
		</div>

		<a href="#sidebar" class="nascondi">Salta contenuto e vai alla <span xml:lang="en">sidebar</span> contenente i <span xml:lang="en">link</span> ad altri siti di scherma e agli <span xml:lang="en">sponsor</span></a>

		<div id="content">
			<div class="article">
					<p>$data</p>
					<p>$luogo</p>
					<h1>$titolo</h1>
					$img
					<p>$paragrafo</p>
					<a href="articoli.cgi">Torna ad articoli</a>
			</div>
		</div>

		<a href="#nav" class="nascondi">Torna al <span xml:lang="fr">menù</span> di navigazione</a>

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
					<li><span class="desc-li">SCHERMA <span xml:lang="en">LINK</span></span>
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
			<img class="footerElement" src="../img/struttura/valid-xhtml11.png" alt="immagine che indica che il sito web è valido come xhtml attraverso la verifica del W3C"/>
			<span class="footerElement">- L'intrusa - <span xml:lang="en">All rights reserved</span> - </span>
			<img class="footerElement" src="../img/struttura/vcss-blue.gif" alt="immagine che indica che lo stile applicato al sito web è valido come css attraverso la verifica del W3C"/>
		</div>

</body>
</html>

EOF
exit;
}