
sub doInserimento{

my $page=new CGI;
# VERIFICA DEI DATI INSERITI

#estraggo la data inserita nella form e la converto in formato YYYY-MM-DD
	my @data=split('/',$page->param('data'));
	my $dataDaSalvare=$data[2].'-'.$data[1].'-'.$data[0];
	my $titolo=$page->param('titolo');
	my $luogo=$page->param('luogo');
	my $testo=$page->param('testo');

	my $fotoNome=$page->upload('foto');
	my $altFoto=$page->param('altfoto');	

	if($page->param('data')=~ m/\d{4}\/\d{2}\/\d{2}/){
		@data=split("/",$page->param('data'));
		$dataDaSalvare=$data[0]."-".$data[1]."-".$data[2];
	}
	else{
		@data=split("-",$page->param('data'));
		$dataDaSalvare=	$page->param('data');
	}

	eval{timelocal(0,0,0,$data[2],$data[1]-1,$data[0]);} || die (&articoloNonCorretto($dataDaSalvare,$titolo,$luogo,$testo));
	
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
		my $nodo;
		eval{$nodo=$parser->parse_balanced_chunk($nuovoArticolo)} || die (&articoloNonCorretto($dataDaSalvare,$titolo,$luogo,$testo));
		$rootDoc->appendChild($nodo);
		open(OUT,">$path");
		print OUT $doc->toString;
		close(OUT);
	}

}


sub articoloNonCorretto{
	open (FILE, "< ../data/private_html/editorArticoli.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;

my $errorField="Ci sono errori nell'inserimento dei dati, controlla tag apertura e chiusura, la data che sia scritta in maniera corretta 
			YYYY-MM-DD(prima l'anno, poi mese,poi giorno)";
$string=~ s/__REINSERISCIFOTO__/Errore nell'inserimento dei dati, reinserisci la foto se l'avevi cambiata/;
$string=~ s/__LUOGO__/$_[2]/;
$string=~ s/__DATA__/$_[0]/;
$string=~ s/__TITOLO__/$_[1]/;
$string=~ s/__TESTO__/$_[3]/;
$string=~ s/__ALT__//;
$string=~ s/__ACTION__/Inserisci Articolo/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__INPUTFOTOVECCHIA__//g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;
$string=~ s/__INCASODIERRORE__/$errorField/;

print $string;

exit;

}


sub blablabla{




#DA USARE PER PROVARE A INSERIRE UN FILE BINARIO COME IMMAGINE O PDF
my $uploadDir="../public_html/img/gare";

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

	open (OUTFILE, ">",$fotoPath) or die "Couldn't open $file for writing: $!";
	binmode (OUTFILE);	
        while ($bytesread = read($fotoNome, $buffer, $num_bytes)) {
            print OUTFILE $buffer;
            print "tra buffer e bytesread";
        }
        close(OUTFILE);
        print OUTFILE $fotoNome;
        print "ciao";
        exit;

	my $fotoSRC="../img/gare/".$foto;
}