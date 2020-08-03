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
        	bat """
        	call BuildTestTools.bat
       		 """
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
