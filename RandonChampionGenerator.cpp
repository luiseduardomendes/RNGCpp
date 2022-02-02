#include "Champions.h"

bool testValidChampion(int roleSearch, int classSearch, Champions champion);
bool testClass(int classSearch, Champions champion);


int main(int argv, char** argc){
    srand(time(NULL));

    

    int numValidChampions = 0;
    int roleSearch = atoi(argc[1]);
    int classSearch = atoi(argc[2]);
    int champSelected, champRandom;

    char *champName;

    Champions champions[NUMCHAMPIONS];

    FILE* dataFile = fopen("saveChampions.sav", "rb");
    fread(champions, sizeof(champions), 1, dataFile);
    fclose(dataFile);

    for (int i = 0; i < NUMCHAMPIONS; i ++)
        if (testValidChampion(roleSearch, classSearch, champions[i]))
            numValidChampions ++;


    champRandom = rand() % numValidChampions;

    std::cout << champRandom << std::endl;  

    int count = 0, j = 0;

    while(count != champRandom) {
        if (testValidChampion(roleSearch, classSearch, champions[j]) && count != champRandom)
            count ++;
        if (count != champRandom)
            j ++;
        else{
            champSelected = j;
        }
    }
    

    champName = champions[champSelected].showName();  

    std::cout << champSelected << " " << champName << std::endl;  
    
    dataFile = fopen("output.txt", "w");
    fprintf(dataFile, "%s", champName);
    fclose(dataFile);
    return 0;
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
        
        default:
            if(testClass(classSearch, champion))
                return true;
            return false;

    }
    return true;
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
        default:
            return true;
    }
    return true;
}