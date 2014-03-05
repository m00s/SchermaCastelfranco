#!/usr/bin/perl -w

use XML::LibXSLT;
use XML::LibXML;
use CGI::Session;
use CGI;
use utf8;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);

do 'login.cgi';

$page=new CGI;
$currentPage=$page->param("pagina");

#controllo lo stato della sessione
$session = CGI::Session->load();
if($session->is_expired or $session->is_empty){
	$session = CGI::Session->new();
	$CGISESSID = $session->id();
}

print $session->header();

#controllo se la form e' stata gia settata
if($page->param("submit")){
	$username = $page->param("username");
	$password = $page->param("password");
	if($username eq 'admin' and $password eq 'admin'){
		$session->param('login', 'admin');
		$session->flush();
		#print "Location: $url\n\n";
		print header('text/html');
		print "<!DOCTYPE HTML> <html><head>";
		print "<link type='text/css' rel='stylesheet' href='../public_html/css/stile.css' media='handheld, screen'/><link type='text/css' rel='stylesheet' href='../public_html/css/print.css' media='braille' />";
		print "</head><body>";
		print $session->header();
		print "<p>Login effettuato con successo</p><META HTTP-EQUIV='Refresh' CONTENT='3; URL=http://www.google.com'>";
		print "</body> </html>";
	}
	else{
		print "Content-type: text/html\n\n";
		print "<!DOCTYPE HTML> <html><head>";
		print "<link type='text/css' rel='stylesheet' href='../style.css' media='handheld, screen'/><link type='text/css' rel='stylesheet' href='../styleAural.css' media='braille' />";
		print "</head><body>";
		print &getLogin();
		print "<p class='error'>Ritenta, sarai pi&ugrave; fortunato!</p>";
		print "</body> </html>";
	}
}
else{
	print "Content-type: text/html\n\n";
	print "<!DOCTYPE HTML> <html><head>";
	print "<link type='text/css' rel='stylesheet' href='../public_html/css/stile.css' media='handheld, screen'/><link type='text/css' rel='stylesheet' href='../public_html/css/print.css' media='braille' />";
	print "</head><body>";
	print &getLogin();
	print "</body> </html>";
}