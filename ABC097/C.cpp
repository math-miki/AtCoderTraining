// まだWA

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string s;
int k;

int compare(string a, string b) {
    // o: a < b 
    // 1: b > a
    // 2: a == b
    int max_index = min(a.size(), b.size());
    for (int i=0; i<max_index; i++) {
        if (a.at(i) == b.at(i)) continue;
        else if (a.at(i) < b.at(i)) return 0;
        else return 1;
    }
    if (a.size() == b.size()) return 2;
    else if (a.size() < b.size()) return 0;
    else return 1;
}

string solve() {
    vector<char> components;
    vector<string> memo;
    for (int i=0; i<s.size(); i++) {
        components.push_back( s.at(i) );
    }
    sort(components.begin(), components.end());
    components.erase(unique(components.begin(), components.end()), components.end());

    for (char letter: components) {
        string::size_type pos = s.find(letter);
        while(pos != std::string::npos) {
            int start = int(pos);
            for(int end = start+1; end<=s.size(); end++) {
                string substring = s.substr(start, end);
                cout << substring << ". ";
                if ( memo.size() == 0 ) memo.push_back(substring);
                else {
                    if ( find(memo.begin(), memo.end(), substring) == memo.end() ) {
                        int i = 0;
                        while (i<memo.size() && compare(substring, memo.at(i))) i++;
                        memo.insert(memo.begin() + i, substring);
                    }
                }
            }
            if (k<=memo.size()) {
                cout << endl;
                for( string candidate: memo) {
                    cout << candidate << ", ";
                }
                cout << endl;
                return memo.at(k-1);
            }
            pos = s.find(letter, pos + 1);
        }

    }
    return "not founr";
}

int main() {
    cin >> s;
    cin >> k;
    cout << solve() << endl;
}
