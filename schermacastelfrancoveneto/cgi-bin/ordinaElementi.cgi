sub ordinaElementiXML
{

	my $file_xsl="../data/ordina.xsl";
	$doc = $parser->parse_file($path);
	$rootDoc= $doc->getDocumentElement;
	#creo il parser
	my $parserSort = XML::LibXML->new();
	#creo l'oggetto per la trasformata
	my $xsltSort = XML::LibXSLT->new();
	#parser dei due documenti
	my $xslt_doc = $parserSort->parse_file($file_xsl);

	#creazione del foglio di trasformazione
	my $stylesheet = $xsltSort->parse_stylesheet($xslt_doc);

	#applicazione del foglio di trasformazione
	my $risultato = $stylesheet->transform($doc);
	my @articoliSort=$risultato->find("//ts:articolo")->get_nodelist();
	my $articoliFinali='';
	foreach $articoloSort(@articoliSort){
		$articoliFinali=$articoloSort->toString().$articoliFinali;
	}

	$articoliFinali=~ s/articolo.*?(>)/articolo>/g;
	my $finalResult="<?xml version=\"1.0\" encoding=\"UTF-8\"?>
					<?xml-stylesheet type=\"text/xsl\" href=\"articoli.xsl\"?>
					<ts:testi xmlns:xs=\"http://www.w3.org/2001/XMLSchema-instance\" 
					xmlns=\"http://www.articoli.com\" xs:schemaLocation=\"http://www.articoli.com articoli.xsd\" 
					xmlns:ts=\"http://www.articoli.com\">".$articoliFinali."</ts:testi>";
	open(OUT,">$path");
	print OUT $finalResult;
	close(OUT);
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=articoli.cgi'>";
	exit;

}