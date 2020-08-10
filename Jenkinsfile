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
		script {
 	        echo %WORKSPACE%
	        echo %BUILD_ID%
	        cd %BUILD_ID%
        	#!/bin/bash
			printf "%-5s %-10s %-4s\n" No Name Mark;
			printf "%-5s %-10s %-4.2f\n" 1 aaa 10.111;
			printf "%-5s %-10s %-4.2f\n" 2 bbb 20.146;
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
