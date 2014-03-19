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

print $string;
}