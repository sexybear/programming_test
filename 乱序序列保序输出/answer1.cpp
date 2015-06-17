#include <iostream>
#include <vector>

using namespace std;

void solve(vector<int> &data)
{
  int start = 1;
  int len = data.size();
  int i = 0;
  int k;

  vector<int>::iterator it;
  vector<int>::iterator be = data.begin();

  while(i < len)
  {
    if(data[i] == start)
    {
      k = data[i];

      cout << setw(5)<< endl;
      it = be + i;

      while(1)
      {
        k++;
        if(find(be,it,k) == it)
        {
          break;
        }

        else
        {
          cout << setw(5)<< k;
        }
      }
      cout << endl;
      start = k;
    }
    i++;
  }
}
