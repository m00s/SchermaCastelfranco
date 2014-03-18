sub getEditor{
	
#ottengo il file HTML da modificare
open (FILE, "< ../data/editorArticoli.html");
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

print $string;
}

sub getEditorDocumento{
open (FILE, "< ../data/editorDocumenti.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
close FILE;

$string=~ s/__TITOLO__//;
$string=~ s/__TESTO__//;
$string=~ s/__DOC__/Non vi sono vecchi documenti inseriti /;

print $string;
}