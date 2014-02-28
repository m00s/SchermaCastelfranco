#!/usr/bin/perl


sub getLogin{
	
#ottengo il file HTML da modificare
my $pagina="../public_html/login.html";
my $parser = XML::LibXML->new();
my $parsedFile = $parser->parse_html_file($pagina);

#estrazione body
my $queryBody = "/*/*[2]/*";
my @body = $parsedFile->findnodes($queryBody);

#serializzazione
my $bodyPagina ='';
foreach $body (@body){
	$bodyPagina .= $body->toString;
}

return $bodyPagina;

}
