pipeline{
    agent any

    stages{
        stage('Build Image'){
            steps{
                sh "docker build -t=nanuvikas/vendor_portal_jenkins ."
            }

        }
        stage('Push Image'){
            steps{
                sh "docker push nanuvikas/vendor_portal_jenkins"
            }
        }
    }

}