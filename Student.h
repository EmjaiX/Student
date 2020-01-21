#ifndef STUDENT_H
#define STUDENT_H
#include <string>
#pragma once

using namespace std;

class Student {
private:
	string FName;
	string LName;
	int CreditHEarned;
	int CreditHAttempted;
	int CreditHPoints;
public:
	Student();
	Student(string Fname,string Lname);
	string getLName() const;
	string getFName() const;
	string getName() const;
};

#endif
