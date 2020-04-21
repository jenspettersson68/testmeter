#!/bin/bash
# Below test script launch JMETER and TODO backend
# Run it with parameter as testfile e.g. ./load_test_run.sh <testfile> 

# Delete containers
docker rm -f jb
docker rm -f todo

# run TODO backend application
docker run -d -t --name todo -p 6078:6078 mesmeratu/todo:latest

#Run Jmeter container linked with TODO backend
docker run -tid --name jb -e TESTFILE=$1 --link todo mesmeratu/jmeter:latest 

# Copy testfile to container
docker cp $1 jb:jmeter/apache-jmeter-5.2.1/bin/$1

# Wait for containers to stabilize
sleep 15

# Run jmeter and generate HTML report
docker exec -i jb bash -c '$JMETER_HOME/bin/jmeter -l $JMETER_HOME/bin/results.csv -e -o report -f -n -t $JMETER_HOME/bin/$TESTFILE'

# Copy report folder to host
docker cp jb:report .
# Xopy csv for jenkinstest
docker cp jb:/jmeter/apache-jmeter-5.2.1/bin/results.csv .
