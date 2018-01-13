#!/bin/bash

source activate data
qpdf --password="" --decrypt testresult.pdf decrypted_testresult.pdf
python pdftestrank.py --id=$1  --path=./decrypted_testresult.pdf
