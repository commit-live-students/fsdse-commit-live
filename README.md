![GitHub Logo](https://s3.ap-south-1.amazonaws.com/greyatom-social/logo.png)

## Lets Get Rolling - Student Pre-Read
Before this lesson , we recommend you go through
* [Integrated_Development Environment](https://en.wikipedia.org/wiki/Integrated_development_environment)

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

## Practice Exercise

* To open this repo inside commit.live execute below command

        clive open
        

* We have encoded build_model.py file inside this repo. It tries to solve one of ML problem using two algorithms.
    * RandomForestClassifier
    * LogisticRegression
* First set value of build = buildRandomForestClassifier and within commit.live IDE enter below command

        clive test

* Test case will fail saying you can improve accuracy
* Now change value of build = buildLogisticRegression and again run above command.
* This time your test case will pass.
* To submit PR and changes to repo use below command:

        clive submit
