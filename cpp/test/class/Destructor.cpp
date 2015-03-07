#include <iostream> 
using namespace std;

class Course{
public:
    Course(){
        cout << "constructing course" << endl;
    }
    ~Course(){
        cout << "destructing course" << endl;
    }
};

class Student{
public:
    Student(int thesemesterHours, double thegpa)
        : semesterHours(thesemesterHours), gpa(thegpa)
    {
        cout << "constructing student" << endl; 
    }
    // delegating constructors
    Student() : Student(0, 0.0) {}
    ~Student(){
        cout << "destructing student" << endl;         
    } 
protected:
    int semesterHours;
    double gpa;
};

class Teacher{
public:
    Teacher(){
        cout << "constructing teacher" << endl; 
    }
    Teacher(const string name){
        cout << "constructing teacher name: " << name << endl; 
    }
    ~Teacher(){
        cout << "destructing teacher" << endl; 
    }
protected:
    Course c;
};


int main(int argc, char const *argv[])
{
    cout << "create an object" << endl;
    Student student;

    cout << "create an object off the heap" << endl;
    Student* pStudent = new Student;
    delete pStudent;

    cout << "create an array of object" << endl;
    Student studentArr[5];

    cout << "create a teacher" << endl;
    Teacher teacher("Jack");
    return 0;
}
