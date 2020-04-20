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
                echo 'run script..'
     //          sh "./load_test_run.sh TODO_backend_test.jmx" 
            }
        }
        stage('Publish report') {
            steps {
                echo 'publish report..'
       // publish html
       //     publishHTML target: [
       //     allowMissing: false,
       //     alwaysLinkToLastBuild: false,
       //     keepAll: true,
       //     reportDir: 'report',
        //    reportFiles: 'index.html',
       //     reportName: 'Performance Test Report'
       //   ]
            }
        }
    }
}
