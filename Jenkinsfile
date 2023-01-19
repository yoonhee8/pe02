pipeline {
  environment {
    imagename = "dockerid/flask_docker:latest"
    theDockerFile = "Dockerfile"
  }
  
  agent any
  
  stages {
    
    
    stage('Cloning Git') {
      steps {
        //need to change "github repo url" and "credentialsId"(created during configuring Jenkins)
        git([url: 'https://github.com/{repo_name}/{repo_name}.git', branch: 'main', credentialsId: 'jenkins-gihub-credential'])
      }
    }
      
    
    stage('Building image') {
      steps{
        script {
          testDockerImage = docker.build("${env.imagename}", "-f ${env.theDockerFile} .")
          //or can simply execute
          //dockerImage = docker.build imagename
        }
      }
    }
    
    
    stage('Remove Unused docker image') {
      steps{
         sh "docker rmi $imagename"
      }
    }
    
    
  }
}