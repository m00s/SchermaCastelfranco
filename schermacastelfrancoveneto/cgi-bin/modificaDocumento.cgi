sub doCaricaFormModificaDocumento{
	

#ottengo il file HTML da modificare
open (FILE, "< ../data/private_html/formModifica.html");
while(!eof(FILE)){
	$form .= <FILE>;
}
close FILE;

#estraggo gli articoli che ci sono e ne mostro data e luogo in cui sono stati effettuati per far selezionare quale cambiare
my $path="../data/documenti.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);
my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);
$xpc->registerNs('ts', 'http://www.documenti.com');
my @documenti=$xpc->find('//ts:documento')->get_nodelist();
my $checkboxdoc;
my $appo;

foreach $documento (@documenti)
{
	my $titolo=$documento->getElementsByTagName("titolo")->get_node(1)->string_value;
	
	
	$appo="
		<input type=\"radio\" name=\"modifica_doc\"
		 value=\"$titolo\"/><label>$titolo</label><br/>
	";

	$checkboxdoc .= $appo;
}

$form=~ s/__DATI__/$checkboxdoc/;
$form=~ s/__TIPO__/Documento/g;
$form=~ s/__VALOREMODIFICA__/CaricaEditorDocumento/;


print $form;
exit;
}


sub doCaricaEditorModificaDocumento{

#ottengo il file HTML da modificare
open (FILE, "<","../data/editorDocumenti.html");
while(!eof(FILE)){
	$editor .= <FILE>;
}
close FILE;

my $page=CGI->new();
#estraggo i valori dalla query string per poi cercare l'articolo voluto
$valore=$page->param("modifica_doc");
my $path="../data/documenti.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);

my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);

$xpc->registerNs('ts', 'http://www.documenti.com');
my @documenti=$xpc->find('//ts:documento')->get_nodelist();

foreach my $node (@documenti) {
	my $titolo=$node->getElementsByTagName("titolo")->get_node(1)->string_value;
	if($titolo eq $valore){
		$docPath=$node->getElementsByTagName("doc-completo")->get_node(1)->string_value;
		my $doc;
		foreach $el (split('/',$docPath)){
			$doc=$el;
		}
		$paragrafo=$node->getElementsByTagName("paragrafo")->item(0)->toString;
		$paragrafo=~ s/\<paragrafo\>//;
		$paragrafo=~ s/\<\/paragrafo\>//;
		$editor=~ s/__TITOLO__/$titolo/g;
		$editor=~ s/__TESTO__/$paragrafo/;
		$editor=~ s/__DOC__/$doc/;
	}

}

$editor=~ s/__VALOREMODIFICA__/SalvaDocumento/;
$editor=~ s/__ACTION__/Salva Documento/;
print $editor;
exit;

}

sub doSalvaDocumento{
my $page=new CGI;
# VERIFICA DEI DATI INSERITI

	# estraggo i vecchi dati che ho salvato nei campi hidden per trovare l'articolo giusto nell'xml
	my $vecchioTitolo=$page->param('vecchioTitolo');
	my $titolo=$page->param('titolo');
	my $testo=$page->param('testo');
	my $doc=$page->param('documento');
	
	my $path="../data/documenti.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);

	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);

	$xpc->registerNs('ts', 'http://www.documenti.com');
	my $query="//ts:documento[ts:titolo=\"$vecchioTitolo\"]";
	my @documenti=$xpc->find($query)->get_nodelist();

	foreach my $node(@documenti){
		$root->removeChild($node);
	}
	my $nuovoDoc="

	<documento>
		<titolo>$titolo</titolo>
		<paragrafo>$testo</paragrafo>
		<doc-completo></doc-completo>
	</documento>

	";

	if($root){

		my $nodo=$parser->parse_balanced_chunk($nuovoDoc) || die "documento non corretto";
		$root->appendChild($nodo);
		open(OUT,">$path");
		print OUT $doc_tree->toString();
	}
}