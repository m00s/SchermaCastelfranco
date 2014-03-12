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

do'eliminaArticolo.cgi';
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

if($page->param('submit') eq "Inserisci Articolo"){

	&doInserimento();
	exit;
}


if($page->param('modifica') eq "CaricaForm"){

	&doCaricaFormModifica();
	exit;	
}
if($page->param('modifica') eq "CaricaEditor"){

	&doCaricaEditorModifica();
	exit;	
}
if($page->param('modifica') eq "SalvaArticolo"){

	&doSalvaArticolo();
	exit;
}


if($page->param('elimina') eq 'CaricaForm'){

	&doCaricaFormElimina();
	exit;	
}
if($page->param('elimina') eq 'SalvaArticolo'){

	&doEliminaArticolo();
	exit;
}

print $page->param("modifica");


&getEditor();
exit;
