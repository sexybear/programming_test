#include <iostream>
#include <stdlib.h>
class myclass1
{
public:
  void run(char *str)
  {
    system(err);
  }

  myclass1()
  {
    std::cout << "myclass1 is created"<<std::endl;
  }
  ~myclass1()
  {
    std::cout << "myclass1 is deleted"<< std::endl;
  }
};

class myclass2
{
  myclass2()
  {
    std::cout << "myclass2 is created"<<std::endl;
  }
  ~myclass2()
  {
    std::cout << "myclass2 is deleted"<< std::endl;
  }
  int add(int a,int b)
  {
    return a+b;
  }
};

class myclass : public myclass1,public myclass2
{

public:
  void print(char *str)
  {
    std::cout << str << std::endl;
  }
  myclass()
  {
    std::cout << "myclass is created"<<std::endl;
  }
  ~myclass()
  {
    std::cout << "myclass is deleted"<< std::endl;
  }
};

void main()
{
  myclass *pmy = new myclass;
  delete pmy;

  std::cin.get();
}

void main1()
{
  myclass my;
  my.run("tasklist");
  my.myclass1::run("ipconfig");
  std::cout << my.add(10,40)<<std::endl;
  my.print("123");

  std::cin.get();
}
