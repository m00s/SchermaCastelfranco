sub doCaricaFormEliminaDocumento{

#ottengo il file HTML da modificare
	open (FILE, "< ../data/formElimina.html");
	while(!eof(FILE)){
	$form .= <FILE>;
	}
	close FILE;

my $path="../data/documenti.xml";
my $parser = XMLin($path);
my $checkboxdoc;
my $appo;

foreach $documento (@{$parser->{documento}})
{
	$titolo=$documento->{titolo};
	
	
	$appo="
		<input type=\"checkbox\" name=\"elimina_doc\"
		 value=\"$titolo\"/><label>$titolo</label><br/>
	";

	$checkboxdoc .= $appo;
}

$form=~ s/__DATI__/$checkboxdoc/;
$form=~ s/__TIPO__/Documenti/g;
$form=~ s/__VALOREELIMINA__/EliminaDocumenti/;


print $form;
exit;


}

sub doEliminaDocumenti{

	my $page=CGI->new();

	my @valori=$page->param("elimina_doc");

	foreach  my $valore (@valori){
		
		$query.="ts:titolo=\"".$valore."\" or ";
	
	}

	$query=	substr $query, 0, -3;

	my $path="../data/documenti.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);

	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);

	$xpc->registerNs('ts', 'http://www.documenti.com');
	@documenti=$xpc->find('//ts:documento['.$query.']')->get_nodelist();
	
	foreach my $documento(@documenti){
		$root->removeChild($documento);
	}

	if($root){

		open(OUT,">$path");
		print OUT $doc_tree->toString();
		close(OUT);
	}

	exit;
}