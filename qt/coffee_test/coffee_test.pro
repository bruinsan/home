#-------------------------------------------------
#
# Project created by QtCreator 2016-11-26T13:59:04
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = coffee_test
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    person.cpp

HEADERS  += mainwindow.h \
    person.h

FORMS    += mainwindow.ui

DISTFILES += \
    coffeedrinkers.xml
