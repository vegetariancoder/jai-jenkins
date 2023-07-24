pipeline {
    agent any

    parameters {
        string(name: 'name', defaultValue: 'Sahil', description: 'username')
        choice(name: 'execution', choices: ['Run', 'NotRun'], description: 'choose a value')
    }
    stages {
        stage('Fetch Parameters') {
            steps {
                echo "Hello ${params.name}"
                echo "desc: ${params.execution}"
            }
        }
        stage('Checkout Branch') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vegetariancoder/jai-jenkins']]])
            }
        }
        stage('Run Pylint') {
            when {
                expression {
                    params.execution == 'Run'
                }
            }
            steps {
                git branch: 'main', url: 'https://github.com/vegetariancoder/jai-jenkins'
                sh 'pylint *.py'
            }
        }
        stage('Build Branch') {
            when {
                expression {
                    params.execution == 'Run'
                }
            }
            steps {
                git branch: 'main', url: 'https://github.com/vegetariancoder/jai-jenkins'
                sh 'python3 running_sum.py'
            }
        }
        stage('Test Branch') {
            when {
                expression {
                    params.execution == 'Run'
                }
            }
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
