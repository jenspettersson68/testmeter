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
                ./load_test_run.sh 
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}