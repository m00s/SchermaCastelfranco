sub getEditor{
	
#ottengo il file HTML da modificare
open (FILE, "< ../public_html/prova_editor.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;
print $string;
}