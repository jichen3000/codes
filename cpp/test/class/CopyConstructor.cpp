#include <iostream>
using namespace std;

class Student
{
public:
    Student(const char *pName = "no name", int ssId = 0)
        : name(pName), id(ssId){
        cout << "Constructed " << name << endl;
    }
    // copy constructor
    Student(const Student& s)
        : name("Copy of " + s.name), id(s.id){
            cout << "copy Constructed " << name << endl;
    }
    ~Student() {
        cout << "Destructing " << name << endl;
    }
    
protected:
    string name;
    int id;
};

void fn(Student copyStudent)
{
    cout << "IN fn() " << endl;
}

class Tutor
{
public:
    Tutor(Student& s)
        : student(s), id(0)
        { cout << "Constructing Tutor object" << endl; } 
protected:
    Student student;
    int id; 
};
void fn(Tutor tutor)
{
    cout << "In function fn()" << endl;
}

int main(int argc, char const *argv[])
{
    Student scruffy("Scruffy", 1234); 
    Tutor tutor(scruffy);
    cout << "Calling fn()" << endl; 
    // fn(scruffy);
    fn(tutor);
    cout << "Back in main()" << endl;    
    return 0;
}