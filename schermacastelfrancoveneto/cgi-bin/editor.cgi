sub getEditor{
	
#ottengo il file HTML da modificare
open (FILE, "< ../data/private_html/editorArticoli.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;


$string=~ s/__LUOGO__//;
$string=~ s/__DATA__//;
$string=~ s/__TITOLO__//;
$string=~ s/__TESTO__//;
$string=~ s/__FOTO__/Non vi sono vecchie foto inserite per questo nuovo articolo/;
$string=~ s/__ALT__//;
$string=~ s/__ACTION__/Inserisci Articolo/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__INPUTFOTOVECCHIA__//g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;

print $string;
}

sub getEditorDocumento{
open (FILE, "< ../data/private_html/editorDocumenti.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
close FILE;

$string=~ s/__TITOLO__//g;
$string=~ s/__TESTO__//;
$string=~ s/__DOC__/Non vi sono vecchi documenti inseriti /;
$string=~ s/__ACTION__/Inserisci Documento/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;
$string=~ s/__INPUTVECCHIODOCUMENTO__//g;
print $string;
}