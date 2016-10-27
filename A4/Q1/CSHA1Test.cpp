#define WIN32_LEAN_AND_MEAN
#define _CRT_SECURE_NO_WARNINGS

#ifdef WIN32
#include <windows.h>
#endif

#include <stdlib.h>
#include <iostream>
#include <string>

#include "CSHA1Test.h"

#include "CSHA1/SHA1.h" // CSHA1 class

using std::endl;

#ifdef _UNICODE
typedef std::wstring tstring;
#define tcout std::wcout
#define tcin std::wcin
#else
typedef std::string tstring;
#define tcout std::cout
#define tcin std::cin
#endif
const tstring characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=";
const int base = 76;

#pragma warning(push)
// Disable compiler warning 'Unreferenced formal parameter'
#pragma warning(disable: 4100)
// Disable compiler warning 'Conditional expression is constant'
#pragma warning(disable: 4127)

int _tmain(int argc, TCHAR* argv[])
{
	tcout << _T("[ Demo application for the CSHA1 class ]") << endl;

	while(true)
	{
		tcout << endl << _T("1) discover my password") << endl;
		tcout << _T("2) Hash a file") << endl;
		tcout << _T("3) discover another password") << endl;
		tcout << _T("4) Exit") << endl << endl;
		tcout << _T("Enter [1], [2] , [3], [4]: ");

		tstring strIn;
		std::getline(tcin, strIn);
		if(strIn.size() == 0) continue;

		const TCHAR ch = strIn[0];

		if(ch == _T('4')) break;
		else if(ch == _T('3')) crackPassword2();
		else if(ch == _T('1')) crackPassword();
		else if(ch == _T('2')) HashFile();
		else tcout << endl << _T("Input error. Enter 1, 2 or 3 and [Enter].") << endl;
	}

	return 0;
}


void crackPassword() {
	tstring salt = "FL";

	int password = 0;

	while(password < 10000) {

		tstring s = std::to_string(password);	

		if(s.size() < 4 ) {

			int i;
			for(i = 0; i< 4 - s.size(); i++) {
				s = "0" + s; 
			}


		}

		s = salt + s; 
		tstring hash = HashString(s);
		if(!hash.compare("C8EA5E1EB0BCDE0F361DA8BB2FAA3E284B941536")) {
			tcout << endl << "password found: " << password << endl;
			break;
		}

		password++;

		if(password % 1000 == 0) {
			tcout << password << "\n";
		}


	}


}

void crackPassword2() {
	tstring salt = "HX";
	int i, j, k, m, n, l;
	tstring s = salt;
	long long count = 0;
	s = salt + characters[0] + characters[0] + characters[0] + characters[0] + characters[0] + characters[0];
	for (i = 0; i < base; i++) {
		//s[i+2] = characters[i];
		for(j = 0; j<base; j++) {
			//s[j+2] = characters[j];
			for(k = 0; k<base; k++) {
				//s[k+2] = characters[k];
				for(l = 0; l<base; l++) {
					//s[l+2] = characters[l];
					for (m = 0; m < base; m++) {
						//s[m + 2] = characters[n];
						for (n = 0; n < base; n++) {
							s.replace(n + 2, 1, tstring(1, characters[n]));
							count++;
							if (count % 100000 == 0) {
								tcout << count << endl;
							}
						}
					}
				}
			}
		}
	}
	
	tcout << endl << s << endl;

   	HashString(s);

}




tstring HashString(tstring s)
{
	//tcout << endl << _T("Enter the string to hash:") << endl;

	tstring str = s;
	// std::getline(tcin, str);
	// tcout << endl;

	CSHA1 sha1;
	tstring strReport;

#ifdef _UNICODE
	const size_t uAnsiLen = wcstombs(NULL, str.c_str(), 0) + 1;
	char* pszAnsi = new char[uAnsiLen + 1];
	wcstombs(pszAnsi, str.c_str(), uAnsiLen);

	sha1.Update((UINT_8*)&pszAnsi[0], strlen(&pszAnsi[0]));
	sha1.Final();
	sha1.ReportHashStl(strReport, CSHA1::REPORT_HEX_SHORT);
	tcout << _T("Hash of the ANSI representation of the string:") << endl;
	tcout << strReport << endl << endl;

	delete[] pszAnsi;
	sha1.Reset();

	sha1.Update((UINT_8*)str.c_str(), str.size() * sizeof(TCHAR));
	sha1.Final();
	sha1.ReportHashStl(strReport, CSHA1::REPORT_HEX_SHORT);
	tcout << _T("Hash of the Unicode representation of the string:") << endl;
	tcout << strReport << endl;
#else
	sha1.Update((UINT_8*)str.c_str(), str.size() * sizeof(TCHAR));
	sha1.Final();
	sha1.ReportHashStl(strReport, CSHA1::REPORT_HEX_SHORT);
	//tcout << _T("String hashed to:") << endl;
	//tcout << strReport << endl;
	return strReport;
#endif
}

void HashFile()
{
	tcout << endl << _T("File path:") << endl;

	tstring strPath;
	std::getline(tcin, strPath);

	CSHA1 sha1;
	const bool bSuccess = sha1.HashFile(strPath.c_str());
	sha1.Final();

	tstring strReport;
	sha1.ReportHashStl(strReport, CSHA1::REPORT_HEX_SHORT);

	if(bSuccess)
	{
		tcout << endl << _T("File contents hashed to:") << endl;
		tcout << strReport << endl;
	}
	else
		tcout << endl << _T("An error occured (does the file really exist?).") << endl;
}

#pragma warning(pop)
