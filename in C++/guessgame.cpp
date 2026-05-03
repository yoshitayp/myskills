#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int number = rand() % 10 + 1;
    int guess;

    cout << "Guess a number between 1 and 10: ";
    cin >> guess;

    if (guess == number)
        cout << "Correct! " << endl;
    else
        cout << "Oops! The number was " << number << endl;

    return 0;
}
