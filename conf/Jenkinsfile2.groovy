pipeline {
    agent {
        kubernetes {
            label "master"
            defaultContainer 'jmeter'
            yamlFile 'conf/k8s-pod.yaml'
        }
    }

    stages {
        stage('blabla') {
            steps {
                echo 'Building..'
            }
        }
        stage('run script') {
            steps {
               sh "./load_test_run2.sh TODO_backend_test.jmx" 
            }
        }
        stage('Publish report') {
            steps {
       // publish html
            publishHTML target: [
            allowMissing: false,
            alwaysLinkToLastBuild: false,
            keepAll: true,
            reportDir: 'report',
            reportFiles: 'index.html',
            reportName: 'Performance Test Report'
          ]
            }
        }
    }
}