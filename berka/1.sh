

URL='http://zho.berka.com/rules/war/tank_counter.gif?redval=255&greenval=255&blueval=255&predef=0&textcol=black&csize=2&tile=N&title=&id=&big2=N&r1=&r2=&r3=&r4=&line1=&line2=&line3=&flip=N&type='

echo Lierka: $1
echo Start: $2
echo Stop: $3


seq $2 $3 | while read A;
do 
	wget $URL$1$A -O $1$A.gif
	sleep 1
done
