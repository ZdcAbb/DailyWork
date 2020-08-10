pipeline {
  agent any
  stages {
    stage('step1') {
      steps {
        echo 'hello world'
      }
    }

    /**************************************************************************/

    stage('Build') {
	steps {
        	sh 'linuxsh.sh'
		}
    }
    stage('step3') {
      steps {
        echo 'hello world 5'
      }
    }
    /**************************************************************************/
  }
}
