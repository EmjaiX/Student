#include "Student.h"
#include <string>

using namespace std;


Student::Student() {

	this->FName = "no";
	this->LName = "name";
	this->CreditHEarned = 0;
	this->CreditHAttempted = 0;
	this->CreditHPoints = 0;
	//simply creates a student object
}

Student::Student(string FName,string LName) {
	this->FName = FName;
	this->LName = LName;
	this->CreditHEarned = 0;
	this->CreditHAttempted = 0;
	this->CreditHPoints = 0;
	//simply creates a student object
}

string Student::getLName() const{
	return LName;
}

string Student::getFName() const{
	return FName;
}

string Student::getName() const{
	return getLName() + ", " + getFName();
}