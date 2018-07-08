pipeline {
  agent {
    docker {
      image 'ankurpatel/tomcat'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'docker build -t ankurpatel/tomcat:V1 .'
      }
    }
  }
}