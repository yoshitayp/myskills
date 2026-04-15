#include <iostream>
using namespace std;

class Student {
    string name;
    int age;
public:
    void input() {
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
    }
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

int main() {
    Student s;
    s.input();
    s.display();
    return 0;
}
