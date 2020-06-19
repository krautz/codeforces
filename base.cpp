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
    lli n_points;
    matriz points;

    // initialize matrix
    for (i = 0; i < n_points; i++)
    {
        // create a vector with 2 positions initialized with 0
        vetor aux (2, 0);

        // here we create a matrix with n_points lines and 2 columns
        points.push_back (aux);
    }

    // sort arrays
    vetor aux (2, 0);
    sort(aux.begin(), aux.end());

    return 0;
}
