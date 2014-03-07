#!/usr/bin/perl -w

use XML::LibXSLT;
use XML::LibXML;
use CGI;
use utf8;
use CGI::Session;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);

$page=new CGI;

my $file_xml="../data/documenti.xml";
my $file_xsl="../data/documenti.xsl";

#creo il parser
my $parser = XML::LibXML->new();
#creo l'oggetto per la trasformata
my $xslt = XML::LibXSLT->new();

#parser dei due documenti
my $doc = $parser->parse_file($file_xml);
my $xslt_doc = $parser->parse_file($file_xsl);

#porto in formato testuale il file dell'xsl
my $query = $xslt_doc->toString;

my $n_documenti=2;

if($page->param('documenti') != 0){
	$n_articoli=$page->param('documenti');
}

#sostituisco nel file xsl quanti articoli far vedere 
$query=~ s/__DOC__/$n_documenti/g;
$xslt_doc = $parser->parse_string($query);

#sostituisco quanti articoli in più fare vedere 
$n_documenti+=2;
$query=~ s/__NDOC__/$n_documenti/g;
$xslt_doc = $parser->parse_string($query);

#creazione del foglio di trasformazione, con sostituzione occorrenza
my $stylesheet = $xslt->parse_stylesheet($xslt_doc);

#applicazione del foglio di trasformazione
my $risultato = $stylesheet->transform($doc);
print "Content-type: text/html\n\n";
print $risultato->toString();