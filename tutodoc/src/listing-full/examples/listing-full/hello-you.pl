print "Qui êtes-vous ? ";
my $name = <STDIN>;

chomp($name);

if ($name eq "") {
    print "Ah, pas très bavard aujourd'hui !\n";

} else {
    print "Bonjour $name.\n";
    print "Épatant ! En fait, pas du tout...\n";
}
