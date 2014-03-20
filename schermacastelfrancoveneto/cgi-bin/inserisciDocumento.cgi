sub doInserimentoDocumento{

	my $page=new CGI;
	# VERIFICA DEI DATI INSERITI

	my $titolo=$page->param('titolo');
	my $testo=$page->param('testo');
	my $documento=$page->param('documento');
	
	my $path="../data/documenti.xml";

	my $parser = XML::LibXML->new();
	my $doc = $parser->parse_file($path);
	my $rootDoc= $doc->getDocumentElement;

	my $nuovoDoc="

	<documento>
		<titolo>$titolo</titolo>
		<paragrafo>$testo</paragrafo>
		<doc-completo></doc-completo>
	</documento>

	";

	if($rootDoc){

		my $nodo;
		eval{$nodo=$parser->parse_balanced_chunk($nuovoDoc)} || die &documentoNonCorretto($titolo,$testo);
		$rootDoc->appendChild($nodo);
		open(OUT,">$path");
		print OUT $doc->toString;
		close(OUT);
	
	}


	#va fatto il caricamento del file pdf come quello della foto
}



sub documentoNonCorrettoInserimento{
	open (FILE, "< ../data/private_html/editorDocumenti.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;

my $errorField="Ci sono errori nell'inserimento dei dati";

$string=~ s/__TITOLO__/$_[0]/;
$string=~ s/__TESTO__/$_[1]/;
$string=~ s/__ACTION__/Inserisci Documento/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;
$string=~ s/__INPUTVECCHIODOCUMENTO__//g;
$string=~ s/__INCASODIERRORE__/$errorField/;

print $string;

exit;

}
