sub doCaricaFormElimina{
	#ottengo il file HTML da modificare
	open (FILE, "< ../data/formElimina.html");
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

	foreach $articolo (@articoli){

		my $data=$articolo->getElementsByTagName("data")->get_node(1)->string_value;
		my $luogo=$articolo->getElementsByTagName("luogo")->get_node(1)->string_value;

		$appo="
			<input type=\"checkbox\" name=\"elimina_articolo\"
			 value=\"".$data."/".$luogo."\"/><label >"
			 .$data." @ ".$luogo."</label></br>
		";

		$checkboxarticoli .= $appo;
	}

	$form=~ s/__DATI__/$checkboxarticoli/;
	$form=~ s/__TIPO__/Articoli/g;
	$form=~ s/__VALOREELIMINA__/EliminaArticoli/;


	print $form;
	exit;

}

sub doEliminaArticoli{

	my $page=CGI->new();


	my @valori=$page->param("elimina_articolo");

	foreach  my $valore (@valori){
		my @dati=split("/", $valore);
	
		$query.="(ts:luogo=\"".$dati[1]."\" and ts:data=\"".$dati[0]."\") or ";
	
	}

	$query=	substr $query, 0, -3;

	my $path="../data/articoli.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);

	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);

	$xpc->registerNs('ts', 'http://www.articoli.com');
	my @articoli=$xpc->find('//ts:articolo['.$query.']')->get_nodelist();
	
	foreach my $articolo(@articoli){
		$root->removeChild($articolo);
	}

	if($root){

		open(OUT,">$path");
		print OUT $doc_tree->toString();
		close(OUT);
		
	}
}
