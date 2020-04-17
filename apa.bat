
REM blablabla

@ECHO OFF

docker rm -f jb
docker rm -f todo

docker run -d -t --name todo -p 6078:6078 ikea-tc/todo:latest

docker run -tid --name jb -e TESTFILE=%1 --link todo ikea-tc/jmeter:latest

docker cp %1 jb:jmeter/apache-jmeter-5.2.1/bin/%1

REM For containers to stabilize
TIMEOUT  20
REM Execute test and create report

docker exec -i jb sh -c "$JMETER_HOME/bin/jmeter -l $JMETER_HOME/bin/results.csv -e -o report -f -n -t $JMETER_HOME/bin/$TESTFILE"

docker cp jb:report .


