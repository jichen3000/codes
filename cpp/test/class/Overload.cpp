#include <iostream>
using namespace std;

class Student
{
public:
    // void calcTuition()
    virtual void calcTuition()
    {
        cout << "We're in Student::calcTuition" << endl;
    }
};

class GraduateStudent : public Student
{
public:
    void calcTuition()
    {
        cout<<"We're in GraduateStudent::calcTuition"<<endl;
    } 
};

void fn(Student& x)
{
    x.calcTuition(); // which calcTuition()?
}

// result using virtual in student:
// We're in Student::calcTuition
// We're in GraduateStudent::calcTuition

// result:
// We're in Student::calcTuition
// We're in Student::calcTuition

int main(int argc, char const *argv[])
{
    // pass a base class object to function 
    // (to match the declaration)
    Student s;
    fn(s);
    // pass a specialization of the base class instead 
    GraduateStudent gs;
    fn(gs);

    return 0;
}