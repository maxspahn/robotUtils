inFile='tempData/out_fks_20210517.csv'
nbFk='1'
awk "NR==${nbFk}" $inFile > temp1.csv
sed 's/;/\n/1' temp1.csv | sed 's/;/\n/3;P;D' > temp2.csv
addedZeros="\n0.0;0.0"
sed '1d' -i temp2.csv
sed '0~4 s/$/\n0.0;0.0/g' temp2.csv > temp3.csv
sed '1 i 0.0;0.0' temp3.csv -i
sed '$d' temp3.csv > tempData/selectedFk_start.csv
nbFk='140'
awk "NR==${nbFk}" $inFile > temp1.csv
sed 's/;/\n/1' temp1.csv | sed 's/;/\n/3;P;D' > temp2.csv
addedZeros="\n0.0;0.0"
sed '1d' -i temp2.csv
sed '0~4 s/$/\n0.0;0.0/g' temp2.csv > temp3.csv
sed '1 i 0.0;0.0' temp3.csv -i
sed '$d' temp3.csv > tempData/selectedFk_140.csv
nbFk='1399'
awk "NR==${nbFk}" $inFile > temp1.csv
sed 's/;/\n/1' temp1.csv | sed 's/;/\n/3;P;D' > temp2.csv
addedZeros="\n0.0;0.0"
sed '1d' -i temp2.csv
sed '0~4 s/$/\n0.0;0.0/g' temp2.csv > temp3.csv
sed '1 i 0.0;0.0' temp3.csv -i
sed '$d' temp3.csv > tempData/selectedFk_end.csv
