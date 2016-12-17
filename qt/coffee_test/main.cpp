#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  MainWindow w;
  w.show();

  // read xml file and create objects (person, etc.)

  std::ifstream myfile ("coffeedrinkers.xml");
  rapidxml::xml_document<> doc;

  doc.parse<0>(myfile);

  std::cout << "Test: " << doc.first_node()->name() << std::endl;



  return a.exec();
}
