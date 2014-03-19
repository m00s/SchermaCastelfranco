sub doInserimento{

my $page=new CGI;
# VERIFICA DEI DATI INSERITI

#estraggo la data inserita nella form e la converto in formato YYYY-MM-DD
	my @data=split('/',$page->param('data'));
	my $dataDaSalvare=$data[2].'-'.$data[1].'-'.$data[0];

	my $titolo=$page->param('titolo');
	my $luogo=$page->param('luogo');
	my $testo=$page->param('testo');
	my $fotoNome=$page->param('foto');
	my $altFoto=$page->param('altfoto');

	my $uploadDir="../public_html/img/gare";


	#setta la grandezza massima della foto
	#$CGI::POST_MAX = 1024 * 5000;

	#stringa da utilizzare nel caso in cui l'utente potesse inserire foto con nome che contenga caratteri non validi come "/"
	#my $caratteri_permessi = "a-zA-Z0-9_.-";

	#faccio parse della stringa passata direttamente dal browser
	#my ( $nome, $path, $estensione ) = fileparse ( $fotoNome, '..*' );
	$foto ="ciao.jpg";

	$foto =~ tr/ /_/; #in caso ci siano spazi nel nome della foto li cambio con degli _ per non creare problemi
	
	#nel caso volessi eseguire il passo di rimuovere dal nome tutti i caratteri che potrebbero dare problemi eseguo 
	#il seguente comando
	#$fotoname =~ s/[^$safe_filename_characters]//g;



	my $fotoPath=$uploadDir."/".$foto;

	#esegue l'upload della foto passata 
	#my $fotoFile = $page->upload("foto");

	#salvo il file dentro la cartella che avevo scelto con il nome scelto
	my ($bytesread, $buffer);
    my $num_bytes = 1024;
    my $totalbytes;
    my $untainted_filename;
	open (OUTFILE, ">", "$fotoPath") or die "Couldn't open $file for writing: $!";

        while ($bytesread = read($fotoNome, $buffer, $num_bytes)) {
            $totalbytes += $bytesread;
            print OUTFILE $buffer;
            print $buffer;
            print $bytesread;
        }
        print "ciao";
        print $page->param('foto')->toString;
        print totalbytes;
        exit;


	my $fotoSRC="../img/gare/".$foto;
	
	#INSERIMENTO DEI DATI VERIFICATI DENTO articoli.xml
	my $path="../data/articoli.xml";
	my $parser = XML::LibXML->new();
	my $doc = $parser->parse_file($path);
	my $rootDoc= $doc->getDocumentElement;

	my $nuovoArticolo="

	<articolo>
		<luogo>".$luogo."</luogo>
		<data>".$dataDaSalvare."</data>
		<titolo>".$titolo."</titolo>
		<img src=\"".$fotoSRC."\" alt=\"".$altFoto."\"/>
		<paragrafo>".$testo."</paragrafo>
	</articolo>

	";

	if($rootDoc){

		my $nodo=$parser->parse_balanced_chunk($nuovoArticolo) || die "articolo non corretto";
		$rootDoc->appendChild($nodo);
		open(OUT,">$path");
		print OUT $doc->toString;
		close(OUT);
	}

}