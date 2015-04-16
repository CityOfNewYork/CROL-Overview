#!/usr/bin/env bash

SRC_DIR="../../../../Current DCAS Implementation/DCAS Database Sample data"

source1="$SRC_DIR/[original] procPublicationRequest Oct-Dec 2014 (2).csv"
source2="$SRC_DIR/[original] procPublicationRequestDMSSPortal Oct-Dec 2014.csv"

target1="orig.procPublicationRequest.oct-dec-2014.csv"
target2="orig.procPublicationRequestDMSSPortal.oct-dec-2014.csv"

[ -e $target1 ] && rm $target1
[ -e $target2 ] && rm $target2

ln -s "$source1" $target1
ln -s "$source2" $target2


