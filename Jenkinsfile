pipeline {
  agent {
    docker {
      image 'ankurpatel/tomcat'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'sudo docker build -t ankurpatel/tomcat:V1 .'
      }
    }
  }
}