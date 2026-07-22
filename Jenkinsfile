pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Clean') {
            steps {
                sh '''
                    rm -rf /var/jenkins_home/workspace/python-qa-project/allure-results
                    mkdir -p /var/jenkins_home/workspace/python-qa-project/allure-results
                '''
            }
        }

        stage('Build tests image') {
            steps {
                sh 'docker compose build tests selenoid'
            }
        }

        stage('Run API tests') {
            steps {
                sh '''
                    docker compose run --rm tests \
                    pytest tests/api -v \
                    --alluredir=/var/jenkins_home/workspace/python-qa-project/allure-results
                '''
            }
        }

        stage('Run UI tests') {
            steps {
                sh '''
                    docker compose up -d selenoid

                    sleep 10

                    docker compose run --rm tests \
                    pytest tests/ui -v \
                    --executor=remote \
                    --browser=chrome \
                    --remote_url=http://selenoid:4444/wd/hub \
                    --alluredir=/var/jenkins_home/workspace/python-qa-project/allure-results
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])

            sh 'docker compose stop selenoid selenoid-ui || true'
        }
    }
}