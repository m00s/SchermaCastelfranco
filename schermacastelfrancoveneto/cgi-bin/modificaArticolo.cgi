sub doCaricaFormModifica{
	
#ottengo il file HTML da modificare
open (FILE, "< ../data/formModifica.html");
while(!eof(FILE)){
	$form .= <FILE>;
}
close FILE;

#estraggo gli articoli che ci sono e ne mostro data e luogo in cui sono stati effettuati per far selezionare quale cambiare
my $path="../data/articoli.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);
my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);
$xpc->registerNs('ts', 'http://www.articoli.com');
my @articoli=$xpc->find('//ts:articolo')->get_nodelist();
my $checkboxarticoli;
my $appo;

foreach $articolo (@articoli)
{
	my $data=$articolo->getElementsByTagName("data")->get_node(1)->string_value;
	my $luogo=$articolo->getElementsByTagName("luogo")->get_node(1)->string_value;
	
	$appo="
		<input type=\"radio\" name=\"modifica_articolo\"
		 value=\"".$data."/".$luogo."\"/><label>"
		 .$data." @ ".$luogo."</label><br/>
	";

	$checkboxarticoli .= $appo;
}

$form=~ s/__DATI__/$checkboxarticoli/;
$form=~ s/__TIPO__/Articolo/g;
$form=~ s/__VALOREMODIFICA__/CaricaEditorArticolo/;

print $form;
exit;

}



sub doCaricaEditorModifica{
#ottengo il file HTML da modificare
open (FILE, "<","../data/editorArticoli.html");
while(!eof(FILE)){
	$editor .= <FILE>;
}
close FILE;

my $page=CGI->new();
#estraggo i valori dalla query string per poi cercare l'articolo voluto
@valori=split("/", $page->param("modifica_articolo"));

print $valori[0]."+".$valori[1];

my $path="../data/articoli.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);

my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);

$xpc->registerNs('ts', 'http://www.articoli.com');
my @articoli=$xpc->find('//ts:articolo')->get_nodelist();

foreach my $node (@articoli) {
	my $data=$node->getElementsByTagName("data")->get_node(1)->string_value;
	my $luogo=$node->getElementsByTagName("luogo")->get_node(1)->string_value;
	if($data eq $valori[0] && $luogo eq $valori[1]){
		my $titolo=$node->getElementsByTagName("titolo")->get_node(1)->string_value;
		my $imgsrc=$node->getElementsByTagName("img")->get_node(1)->getAttribute("src");
		my $img;
		foreach $el (split('/',$imgsrc)){
			$img=$el;
		}
		my $imgalt=$node->getElementsByTagName("img")->get_node(1)->getAttribute("alt");
		my $paragrafo=$node->getElementsByTagName("paragrafo")->item(0)->toString;
		$paragrafo=~ s/\<paragrafo\>//;
		$paragrafo=~ s/\<\/paragrafo\>//;
		$editor=~ s/__LUOGO__/$luogo/g;
		$editor=~ s/__DATA__/$data/g;
		$editor=~ s/__TITOLO__/$titolo/;
		$editor=~ s/__TESTO__/$paragrafo/;
		$editor=~ s/__FOTO__/$img/g;
		$editor=~ s/__ALT__/$imgalt/;
		
	}

}
$editor=~ s/__ACTION__/Salva Articolo/;
$editor=~ s/__VALOREMODIFICA__/SalvaArticolo/;

print $editor;
exit;
}



sub doSalvaArticolo{
my $page=new CGI;
# VERIFICA DEI DATI INSERITI

	# estraggo i vecchi dati che ho salvato nei campi hidden per trovare l'articolo giusto nell'xml
	my $datavecchia=$page->param('vecchiaData');
	my $vecchioluogo=$page->param('vecchioLuogo');

	my @data=split('/',$page->param('data'));
	my $dataDaSalvare=$data[2].'-'.$data[1].'-'.$data[0];

	my $titolo=$page->param('titolo');
	my $luogo=$page->param('luogo');
	my $testo=$page->param('testo');
	my $fotoNome=$page->param('foto');
	my $altFoto=$page->param('altfoto');
	my $uploadDir="../img/gare";
	my $fotoPath;

	if($page->param('foto')){
		print "hello";
		#faccio parse della stringa passata direttamente dal browser
		my ( $nome, $path, $estensione ) = fileparse ( $fotoNome, '..*' );
		$fotoNome = $nome.$estensione;

		$fotoNome =~ tr/ /_/; #in caso ci siano spazi nel nome della foto li cambio con degli _ per non creare problemi
		#nel caso volessi eseguire il passo di rimuovere dal nome tutti i caratteri che potrebbero dare problemi eseguo 
		#il seguente comando

		#$fotoname =~ s/[^$safe_filename_characters]//g;

		$fotoPath=$uploadDir."/".$fotoNome;

		
		#esegue l'upload della foto passata 
		my $fotoFile = $page->upload("foto");

		#fare upload foto sul server


	}
	else{
		$fotoPath=$uploadDir."/".$page->param("vecchiaFoto");
	}
	
	my $path="../data/articoli.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);
	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);
	$xpc->registerNs('ts', 'http://www.articoli.com');
	my $query="//ts:articolo[ts:luogo=\"$vecchioluogo\" and ts:data=\"$datavecchia\"]";
	my @articoli=$xpc->find($query)->get_nodelist();

	foreach my $node(@articoli){
		$root->removeChild($node);
		
	}
	my $nuovoArticolo="

	<articolo>
		<luogo>".$luogo."</luogo>
		<data>".$dataDaSalvare."</data>
		<titolo>".$titolo."</titolo>
		<img src=\"".$fotoPath."\" alt=\"".$altFoto."\"/>
		<paragrafo>".$testo."</paragrafo>
	</articolo>

	";

	if($root){

		my $nodo=$parser->parse_balanced_chunk($nuovoArticolo) || die "articolo non corretto";
		$root->appendChild($nodo);
		open(OUT,">$path");
		print OUT $doc_tree->toString();
		close(OUT);
	}

}
