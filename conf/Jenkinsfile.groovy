pipeline {
    agent any

    stages {
        stage('blabla') {
            steps {
                echo 'Building..'
            }
        }
        stage('run script') {
            steps {
               sh "./load_test_run.sh TODO_backend_test.jmx" 
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