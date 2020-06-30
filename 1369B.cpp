#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdlib.h>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <queue>

using namespace std;

typedef long long int lli;
typedef vector <lli> vetor;
typedef vector <vector <lli> > matriz;

int main ()
{
    lli testCases, size, pos, solutionSize;
    char str[1000002], solution[100002];
    string strAux;
    bool one, zero;

    cin >> testCases;

    while (testCases > 0) {

        cin >> size;

        cin >> strAux;

        for (lli i = size - 1; i >= 0; i--) {
            str[i] = strAux[i];
        }

        solutionSize = -1;

        one = false;
        zero = false;
        pos = -1;
        for (lli i = size - 1; i >= 0; i--) {

            if (str[i] == '1' && one == false && zero == false) {
                solutionSize++;
                solution[solutionSize] = '1';
            }

            if (str[i] == '0' && one == false && zero == false) {
                zero = true;
                pos = i;
            }

            if (str[i] == '1' && one == false && zero == true) {
                one = true;
            }

            if (str[i] == '0' && one == true && zero == true) {
                str[i + 1] = '0';
                pos = i + 1;
                one = false;
            }
        }

        if (one == false && zero == true) {

            for (lli i = 0; i <= pos; i++) {
                cout << str[i];
            }

            for (lli i = solutionSize; i >= 0; i--) {
                cout << solution[i];
            }

            cout << endl;
        }

        else if (one == true && zero == true) {
            cout << '0';

            for (lli i = solutionSize; i >= 0; i--) {
                cout << solution[i];
            }

            cout << endl;
        }

        else if (one == false && zero == false) {
            for (lli i = solutionSize; i >= 0; i--) {
                cout << solution[i];
            }
            cout << endl;
        }
        testCases--;
    }

    return 0;
}
