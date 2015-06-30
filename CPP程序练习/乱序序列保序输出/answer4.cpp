void solution(vector<int> &data)  
{  
    int start = 1;  
    int len = data.size();  
    int i = 0;  
    bool flag = 0;  
    map<int, int> mp;  
    while (i < len)  
    {  
        mp[data[i]] = 1;  
        while (mp[start] == 1)  
        {  
            flag = 1;  
            cout << setw(5) << start;  
            start++;  
        }  
        if (flag)  
        {  
            cout << endl;  
            flag = 0;  
        }  
        i++;  
    }  
}  
