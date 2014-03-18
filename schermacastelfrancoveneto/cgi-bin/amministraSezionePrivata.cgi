#!/usr/bin/perl -w

use strict;
use XML::LibXSLT;
use XML::LibXML;
use CGI::Session;
use CGI;
use utf8;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);
use File::Basename;

do 'eliminaDocumenti.cgi';
do 'modificaDocumento.cgi';
do 'inserisciDocumento.cgi';
do 'selezionaCosa.cgi';
do 'ordinaElementi.cgi';
do 'eliminaArticolo.cgi';
do 'modificaArticolo.cgi';
do 'inserisciArticolo.cgi';
do 'editor.cgi';
do 'login.cgi';

print "Content-type: text/html\n\n";
my $page=CGI->new();

#controllo lo stato della sessione
my $session = CGI::Session->load();
if(!$session->is_expired && !$session->is_empty){
}


#una volta scelto se modifica un articolo carico la pagina adeguata per inserire,modificare o eliminare articoli

if($page->param('Inserisci'))
{
	if($page->param('cosa') eq "articolo"){

		&getEditor();
		exit;	
	}
	if($page->param('cosa') eq "documento"){

		&getEditorDocumento();
		exit;	
	}
}
if($page->param('Modifica'))
{
	if($page->param('cosa') eq "articolo"){

		&doCaricaFormModifica();
		exit;	
	}
	if($page->param('cosa') eq "documento"){

		&doCaricaFormModificaDocumento();
		exit;	
	}
}
if($page->param('Elimina'))
{
	if($page->param('cosa') eq "articolo"){

		&doCaricaFormElimina();
		exit;	
	}
	if($page->param('cosa') eq "documento"){

		&doCaricaFormEliminaDocumento();
		exit;	
	}
}




if($page->param('submit') eq "Inserisci Articolo"){

	&doInserimento();
	&ordinaElementi();
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=articoli.cgi'>";
	exit;
}

if($page->param('submit') eq "Inserisci Documento"){

	&doInserimentoDocumento();
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=documenti.cgi'>";
	exit;
}


if($page->param('modifica') eq "CaricaEditorArticolo"){

	&doCaricaEditorModifica();
	exit;	
}
if($page->param('modifica') eq "SalvaArticolo"){

	&doSalvaArticolo();
	&ordinaElementi();
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=articoli.cgi'>";
	exit;
}
if($page->param('modifica') eq "CaricaEditorDocumento"){

	&doCaricaEditorModificaDocumento();
	exit;	
}
if($page->param('modifica') eq "SalvaDocumento"){

	&doSalvaDocumento();
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=documenti.cgi'>";
	exit;
}



if($page->param('elimina') eq 'EliminaDocumenti'){

	&doEliminaDocumenti();
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=documenti.cgi'>";
	exit;
}

if($page->param('elimina') eq 'EliminaArticoli'){

	&doEliminaArticoli();
	&ordinaElementi();
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=articoli.cgi'>";
	exit;
}

&selezionaCosa();
exit;