#!/usr/bin/perl
use File::Basename;

#take a list of file names output distance and avg RSSI
foreach my $f (@ARGV) {
    #open the file and get the average for each line
    open F,"<", $f or die "Can not open $f\n";
    my $total = 0;
    my $count = 0;
    
    foreach my $line (<F>) {
        chomp $line;
        $total += int($line); 
        $count++;
    }
    
    #calculate average and output distanc and RSSI
    my $avg = $total/$count;
    $avg=sprintf("%.2f", $avg);
    $f = basename($f);
    $f =~ /(.*)\.txt/;
    print "$1 $avg\n";
    close F;
}

