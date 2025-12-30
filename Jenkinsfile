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
                        pip install --upgrade pip --break-system-packages
                        pip install -r requirements.txt --break-system-packages
                        pip install pytest pytest-cov --break-system-packages
                    '''
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    echo '========== Running Unit Tests =========='
                    sh '''
                        export PATH="/var/jenkins_home/.local/bin:$PATH"
                        export PYTHONPATH=".:$PYTHONPATH"
                        export PYTHONUSERBASE="/var/jenkins_home/.local"
                        pwd
                        ls -la
                        python3 -m pytest test_app.py -v --cov=app --cov-report=html --cov-report=term --import-mode=importlib
                    '''
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    echo '========== Building Application =========='
                    sh '''
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
