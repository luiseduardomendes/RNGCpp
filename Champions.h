#pragma once
#define NUMCHAMPIONS 155
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

enum{TOPLANE, JUNGLE, MIDLANE, ADCARRY, SUPPORT};
enum{ROGUE, MAGE, FIGHTER, MARKSMAN, CONTROLL, TANK};

typedef struct {
    char nameChampion[20];
    bool classAttributes[6];
    bool roleAttributes[5];
}t_dataChampion;

class Champions{
private:
    t_dataChampion dataChampion;
public:
    void createChampion(char name[20]);
    void addClassChampion(int classChamp);
    void addRoleChampion(int roleChamp);

    bool isTopLane();
    bool isJungle();
    bool isMidLane();
    bool isAdCarry();
    bool isSupport();

    bool isRogue();
    bool isMage();
    bool isFighter();
    bool isMarksman();
    bool isControll();
    bool isTank();

    void ShowChampionInfo();
    void storageChampion();
    void loadChampionData(FILE* dataFile);
};