#!/usr/bin/perl -w
use XML::LibXML;
use HTML::Entities;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

#redirezione
my $url = "http://tecnologie-web.studenti.math.unipd.it/tecweb/~mpavanel/index.html";
print "Location: $url\n\n";
