#include "Champions.h"

bool testValidChampion(int roleSearch, int classSearch, Champions champion);
bool testClass(int classSearch, Champions champion);


int main(int argv, char** argc){
    srand(time(NULL));

    int numValidChampions = 0;
    int roleSearch = atoi(argc[1]);
    int classSearch = atoi(argc[2]);
    int champSelected;

    Champions champions[NUMCHAMPIONS];

    FILE* dataFile = fopen("saveChampions.sav", "rb");
    fread(champions, sizeof(champions), 1, dataFile);
    fclose(dataFile);

    for (int i = 0; i < NUMCHAMPIONS; i ++)
        if (testValidChampion(roleSearch, classSearch, champions[i]))
            numValidChampions ++;


    champSelected = rand() % numValidChampions;
    
    std::cout << champSelected << std::endl;
}

bool testValidChampion(int roleSearch, int classSearch, Champions champion){
    switch (roleSearch) {
        case TOPLANE:
            if(champion.isTopLane() && testClass(classSearch, champion))
                return true;
            return false;

        case JUNGLE:
            if(champion.isJungle() && testClass(classSearch, champion))
                return true;
            return false;

        case MIDLANE:
            if(champion.isMidLane() && testClass(classSearch, champion))
                return true;
            return false;

        case ADCARRY:
            if(champion.isAdCarry() && testClass(classSearch, champion))
                return true;
            return false;

        case SUPPORT:
            if(champion.isSupport() && testClass(classSearch, champion))
                return true;
            return false;

    }
    return false;
}

bool testClass(int classSearch, Champions champion){
    switch (classSearch) {
        case ROGUE:
            if(champion.isRogue())
                return true;
            return false;
            break;
        case MAGE:
            if(champion.isMage())
                return true;
            return false;
            break;
        case FIGHTER:
            if(champion.isFighter())
                return true;
            return false;
            break;
        case MARKSMAN:
            if(champion.isMarksman())
                return true;
            return false;
            break;
        case CONTROLL:
            if(champion.isControll())
                return true;
            return false;
            break;
        case TANK:
            if(champion.isTank())
                return true;
            return false;
            break;
    }
    return false;
}