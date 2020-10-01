// C++ program to illustrate the
// unordered_multiset::erase() function

#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    unordered_multiset<int> samplemultiSet;

    // Inserting elements
    samplemultiSet.insert(10);
    samplemultiSet.insert(5);
    samplemultiSet.insert(15);
    samplemultiSet.insert(20);
    samplemultiSet.insert(25);
    samplemultiSet.insert(10);
    samplemultiSet.insert(15);
    samplemultiSet.insert(20);

    // Erases a particular element by its position
    samplemultiSet.erase(samplemultiSet.begin());

    // Displaying the set after removal
    for (auto it = samplemultiSet.begin(); it != samplemultiSet.end(); it++) {
        cout << *it << " ";
    }

    cout << endl;
    // erases a range of elements,
    // here all the elements
    auto itr = samplemultiSet.find(15);
    if (itr != samplemultiSet.end()) {
        samplemultiSet.erase(itr);
    }

    for (auto it = samplemultiSet.begin(); it != samplemultiSet.end(); it++) {
        cout << *it << " ";
    }

    cout << "\nMultiSet size: " << samplemultiSet.size() << endl;

    return 0;
}
