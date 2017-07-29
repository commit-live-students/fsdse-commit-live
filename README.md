![GitHub Logo](https://s3.ap-south-1.amazonaws.com/greyatom-social/logo.png)

## Let's Get Rolling - Student Pre-Read
Before this lesson, we recommend you go through
* [Integrated Development Environment](https://en.wikipedia.org/wiki/Integrated_development_environment)

## Learning Objectives

After this lesson, you'll be able to
* Use Commit.Live Web App
* Use Commit.Live IDE
* Use Commit.Live CLI

## Agenda

* Why Commit.Live ?
* Comit.Live Platform
* Comit.Live Web Application
* Comit.Live IDE 
* Comit.Live Command Line (CLI) 
* Practice Exercise

## Slides
@[gslides](1gEb00r1CyjxWignP0JC84UArH7qny05p-CQhMdBcu2o)

## Download 
* [Download for Linux](https://github.com/greyatom-edu-tech/greyatom-ide/releases/download/v4.4.10/commit_live-amd64.deb)
  * If Atom is already installed this will replace your Atom, please save your settings if you have any
  * To install use command `sudo dpkg -I <downloaded-file-path>` 
* [Download for MacOS X](https://github.com/greyatom-edu-tech/greyatom-ide/releases/download/v4.4.10/CommitLive.dmg)

## Practice Exercise

* Let's do a small exercise to see how Commit.Live web application, IDE and CLI works together
* Navigate to web application dashboard and click on continue button under current course. This will take you to lesson page.
* To open this repo inside Commit.Live IDE click on `Open in app` button on lesson page and copy the open command which will look like below 

        clive open fsdse-commit-live
        
* Run above command in Commit.Live IDE terminal
* Let's quickly go through what we have in repo

         data - Contains dummy data set
         test - Contains test cases
         build_model.py - File which we are going to run and test
         README.md - Readme file
         
* build_model.py tries to solve one of ML problem using two algorithms below:
    * RandomForestClassifier
    * LogisticRegression
* We will first run test cases present in the test folder and see test case output.Open terminal and run test command
        
        clive test

* This will run test cases against the build_model.py file. Your test case will fail ans say you can improve accuracy even more
* Now open build_model.py and change build method to buildLogisticRegression. You last line in build_model.py should look like below:

          build = buildLogisticRegression
          
* Now again run test command again.This time your test case will pass
* To submit PR and changes to repo use below command:

        clive submit
