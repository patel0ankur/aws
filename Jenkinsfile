pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('') {
      steps {
        sh 'docker build -t ankurpatel/tomcat:V1 .'
      }
    }
  }
}