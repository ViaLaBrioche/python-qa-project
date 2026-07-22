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
                    rm -rf allure-results
                    mkdir -p allure-results
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
                    --alluredir=allure-results/api
                '''
            }
        }

        stage('Run UI tests') {
            steps {
                sh '''
                    pwd
                    ls -la
                    ls -la selenoid || true

                    docker compose up -d selenoid

                    sleep 10

                    docker compose ps
                    docker compose logs selenoid

                    docker compose run --rm tests \
                    pytest tests/ui -v \
                    --executor=remote \
                    --browser=chrome \
                    --remote_url=http://selenoid:4444/wd/hub \
                    --alluredir=allure-results/ui
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