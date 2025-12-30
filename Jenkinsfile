pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13'
        APP_NAME = 'flask-student-app'
        BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo '========== Cloning Repository =========='
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/${BRANCH}']],
                        userRemoteConfigs: [[url: 'https://github.com/i221608-prog/flask.git']]
                    ])
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo '========== Installing Dependencies =========='
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate.bat
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
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest test_app.py -v --cov=. --cov-report=html --cov-report=term
                    '''
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    echo '========== Building Application =========='
                    bat '''
                        call venv\\Scripts\\activate.bat
                        echo Build artifacts generated successfully
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    echo '========== Deploying Application =========='
                    bat '''
                        call venv\\Scripts\\activate.bat
                        echo Application deployed successfully
                        echo You can modify this stage to deploy to your target environment
                        echo Examples: Docker, AWS, Heroku, etc.
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
