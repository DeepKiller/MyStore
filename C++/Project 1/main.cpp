#include <WinSock2.h>
#include <iostream>
using namespace std;
int main(){   
    
    return 0;
}
class Server{
    public:
    void startUp(){
        if(WSAStartup(MAKEWORD(2,2),&wData)==0){
            printf("WSA startup");
        }
    }
    private:
        WSADATA wData;
};