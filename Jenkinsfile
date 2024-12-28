pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                sh 'docker pull urmsandeep/ai-artistic-style-service:latest'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm -p 5001:5001 urmsandeep/ai-artistic-style-service bash -c "pip install pytest && pytest tests/"
                '''
            }
        }
        stage('Deploy Service') {
            when {
                expression { currentBuild.result == null }
            }
            steps {
                sh 'docker-compose down && docker-compose up -d'
            }
        }
        stage('Verify Deployment') {
            when {
                expression { currentBuild.result == null }
            }
            steps {
                sh '''
                    if [ ! -f test.jpg ]; then
                        echo "test.jpg not found!"
                        exit 1
                    fi
                    curl -X POST http://127.0.0.1:5001/styleTransfer -F "image=@test.jpg" --output styled_output.jpg
                '''
            }
        }
    }
    post {
        always {
            sh 'docker system prune --filter "until=24h" -f'
        }
    }
}
