pipeline {
  agent any
  stages {
    stage('Hello') {
      steps {
        sh 'echo "Hello World"'
      }
    }
    stage('Docker') {
      steps {
        sh ' docker pull ankurpatel/tomcat'
      }
    }
  }
}