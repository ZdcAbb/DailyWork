pipeline {
  agent any
  stages {
    stage('step1') {
      steps {
        echo 'hello world'
      }
    }

    /**************************************************************************/

    stage('step2') {
	steps {
 	    echo %WORKSPACE%
	    echo %BUILD_ID%
	    cd %BUILD_ID%


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
