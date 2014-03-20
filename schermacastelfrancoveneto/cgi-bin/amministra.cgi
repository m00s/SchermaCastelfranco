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
if($page->param('logout') eq "esci"){
	$session->close();
	$session->delete();
	$session->flush();
	print $session->header(-location=>"articoli.cgi");
	exit;
}

if($session->is_expired or $session->is_empty){
	$session = new CGI::Session;

	#controllo se la form e' stata gia settata
	if($page->param("submit")){
		$username = $page->param("username");
		$password = $page->param("password");
		if($username eq 'admin' and $password eq 'admin'){
			$session->param('login', 'admin');
			print $session->header(-location=>"amministraSezionePrivata.cgi");
			exit;
		}
		else{
			print "Content-type: text/html\n\n";
			print &getLogin();
			exit;
		}
	}
	else{

		print "Content-type: text/html\n\n";
		print &getLogin();
		exit;
	}
}
else{
	print $session->header(-location=>"amministraSezionePrivata.cgi");
	exit;
}