pipeline {
  agent none
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
            BuildTestTools.bat
        """
        // Parallel?
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
