#!/bin/bash
f=$1
echo $f
sed 's/.$/\]/g' $f |sed 's/^./\[/g'
