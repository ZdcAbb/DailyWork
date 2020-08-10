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
 	    echo "hello\n world"
		echo -e "hello\n world"

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
