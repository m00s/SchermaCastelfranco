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

		my $nodo=$parser->parse_balanced_chunk($nuovoDoc) || die "articolo non corretto";
		$rootDoc->appendChild($nodo);
		open(OUT,">$path");
		print OUT $doc->toString;
		close(OUT);
	
	}


	#va fatto il caricamento del file pdf come quello della foto
}