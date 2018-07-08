pipeline {
  agent {
    docker {
      image 'ankurpatel/tomcat'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'sudo docker pull ankurpatel/tomcat'
      }
    }
  }
}