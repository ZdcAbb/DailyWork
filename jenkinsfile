pipeline {
  agent none
  stages {
    stage('step1') {
      steps {
        echo 'hello world'
      }
    }

    stage('step2') {
      steps {
        bat(script: 'build_1.bat', returnStatus: true)
      }
    }

  }
}