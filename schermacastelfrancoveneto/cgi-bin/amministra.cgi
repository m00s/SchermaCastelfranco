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

# print $session->header();

#controllo se la form e' stata gia settata
if($page->param("submit")){
	$username = $page->param("username");
	$password = $page->param("password");
	if($username eq 'admin' and $password eq 'admin'){
		$session->param('login', 'admin');
		$session->flush();
		print $session->header();
		print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=amministraSezionePrivata.cgi'>";
	}
	else{
		print "Content-type: text/html\n\n";
		print &getLogin();
		# print "<p class='error'>Ritenta, sarai pi&ugrave; fortunato!</p>";
	}
}
else{

	print "Content-type: text/html\n\n";
	print &getLogin();

}