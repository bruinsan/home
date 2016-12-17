#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <iostream>
#include <fstream>
#include <string>
#include "../../../Downloads/rapidxml-1.13/rapidxml.hpp"

namespace Ui {
  class MainWindow;
}

class MainWindow : public QMainWindow
{
  Q_OBJECT

public:
  explicit MainWindow(QWidget *parent = 0);
  ~MainWindow();

private slots:
  void on_addCoffee_clicked();

private:
  Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
