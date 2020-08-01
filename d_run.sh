#!/bin/sh

e=$1
fL=$2
lr=$3
d=$4
logFileName="output_e${e}_fL${fL}_lr${lr}_d${d}"


script -c model_run -e ${e} -fragmentLen $fL -lr $lr --decay $d 
