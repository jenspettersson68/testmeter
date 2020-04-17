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
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}