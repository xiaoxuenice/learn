for i in `seq 1 10000`;do unzip -P $i xx.zip -d $i ;if [ $? -eq 0 ];then echo $i > a.txt && exit;fi;done
