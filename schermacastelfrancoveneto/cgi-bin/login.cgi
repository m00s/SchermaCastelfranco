sub getLogin{

#ottengo il file HTML da modificare
open (FILE, "<","../data/private_html/pagLogin.html");
while(!eof(FILE)){
	$pagina .= <FILE>;
}

close FILE;

# $pagina=~ s/_ERRORE_/Valori errati/;

return $pagina;
}
