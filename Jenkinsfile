pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13'
        APP_NAME = 'flask-student-app'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo '========== Cloning Repository =========='
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[url: 'https://github.com/i221608-prog/ssdfinal.git']]
                    ])
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo '========== Installing Dependencies =========='
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip install pytest pytest-cov
                    '''
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    echo '========== Running Unit Tests =========='
                    sh '''
                        . venv/bin/activate
                        pytest test_app.py -v --cov=app --cov-report=html --cov-report=term
                    '''
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    echo '========== Building Application =========='
                    sh '''
                        . venv/bin/activate
                        echo "Build artifacts generated successfully"
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    echo '========== Deploying Application =========='
                    sh '''
                        . venv/bin/activate
                        echo "Application deployed successfully"
                        echo "You can modify this stage to deploy to your target environment"
                        echo "Examples: Docker, AWS, Heroku, etc."
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                echo '========== Pipeline Execution Completed =========='
            }
        }
        success {
            script {
                echo '========== Build Successful =========='
            }
        }
        failure {
            script {
                echo '========== Build Failed =========='
            }
        }
    }
}
