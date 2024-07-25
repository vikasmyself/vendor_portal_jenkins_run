pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
            stage('Run Tests'){
                steps{
                    sh "docker-compose -f grid.yaml up -d"
                }
            }
            stage('Bring Grid down'){
                steps{
                    sh "docker-compose -f test-suites.yaml up"
                }
            }

    }
    post{
        always {
            sh "docker-compose -f grid.yaml down -d"
            sh "docker-compose -f test-suites.yaml down"
        }
    }
}
