sub selezionaCosa{

	my $page=new CGI;

	if($page->param('Seleziona') eq "modifica"){

		open (FILE, "<","../data/selectModifica.html");
		while(!eof(FILE)){
			$editor .= <FILE>;
		}
		close FILE;
		print $editor;
		exit;
	}

	if($page->param('Seleziona') eq "elimina"){

		open (FILE, "<","../data/selectElimina.html");
		while(!eof(FILE)){
			$editor .= <FILE>;
		}
		close FILE;
		print $editor;
		exit;
	}

#se non è nessuna tra modifica o elimina, di default faccio vedere inserisci
open (FILE, "<","../data/selectInserisci.html");
	while(!eof(FILE)){
		$editor .= <FILE>;
	}
	close FILE;
	print $editor;
	exit;
}