pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
            stage('Run Tests'){
                steps{
                    sh "docker-compose up"
                }
            }
            stage('Bring Grid down'){
                steps{
                    sh "docker-compose down"
                }
            }

    }
}
