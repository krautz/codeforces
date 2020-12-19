// TLE test 3

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

int main() {
    lli i, j, longest, n, x, t, sum;

    cin >> t;

    while (t > 0) {

        cin >> n >> x;

        vetor elements(n);

        for (i = 0; i < n; i++) {
            cin >> elements[i];
        }

        longest = -1;

        for (i = 0; i < n; i++) {

            sum = elements[i];

            if (sum % x != 0 && longest == -1) {
                longest = 1;
            }

            if (n - i <= longest) {
                continue;
            }

            for (j = i + 1; j < n; j++) {

                sum += elements[j];

                if (sum % x != 0 && (j - i + 1) > longest) {
                    longest = (j - i + 1);
                }
            }
        }

        cout << longest << endl;

        t--;
    }
    return 0;
}
