#include "Champions.h"


bool Champions::isTopLane(){
    if (dataChampion.roleAttributes[TOPLANE])
        return true;
    else
        return false;
}
bool Champions::isJungle(){
    if (dataChampion.roleAttributes[JUNGLE])
        return true;
    else
        return false;
}
bool Champions::isMidLane(){
    if (dataChampion.roleAttributes[MIDLANE])
        return true;
    else
        return false;
}
bool Champions::isAdCarry(){
    if (dataChampion.roleAttributes[ADCARRY])
        return true;
    else
        return false;
}
bool Champions::isSupport(){
    if (dataChampion.roleAttributes[SUPPORT])
        return true;
    else
        return false;
}

bool Champions::isRogue(){
    if (dataChampion.classAttributes[ROGUE])
        return true;
    else
        return false;
}
bool Champions::isFighter(){
    if (dataChampion.classAttributes[FIGHTER])
        return true;
    else
        return false;
}
bool Champions::isMage(){
    if (dataChampion.classAttributes[MAGE])
        return true;
    else
        return false;
}
bool Champions::isMarksman(){
    if (dataChampion.classAttributes[MARKSMAN])
        return true;
    else
        return false;
}
bool Champions::isControll(){
    if (dataChampion.classAttributes[CONTROLL])
        return true;
    else
        return false;
}
bool Champions::isTank(){
    if (dataChampion.classAttributes[TANK])
        return true;
    else
        return false;
}

void Champions::createChampion(char name[20]){
    strcpy(dataChampion.nameChampion, name);
    for (int i = 0; i < 5; i++){
        dataChampion.roleAttributes[i] = false;
    }
    for (int i = 0; i < 6; i++){
        dataChampion.classAttributes[i] = false;
    }

}

void Champions::addClassChampion(int classChamp){
    if (!dataChampion.classAttributes[classChamp]){
        dataChampion.classAttributes[classChamp] = true;
    }
}

void Champions::addRoleChampion(int roleChamp){
    if (!dataChampion.roleAttributes[roleChamp]){
        dataChampion.roleAttributes[roleChamp] = true;
    }
}

void Champions::ShowChampionInfo(){
    std::string rolesStr[] = {"Top Lane", "Jungle", "Mid Lane", "Ad Carry", "Support"};
    std::string classesStr[] = {"Assassino", "Mago", "Lutador", "Atirador", "Suporte", "Tanque-"};
    std::cout << std::endl << dataChampion.nameChampion << std::endl;
    std::cout << "Roles: ";
    for (int i = 0; i < 5; i++)
        if (dataChampion.roleAttributes[i])
            std::cout << rolesStr[i] << " ";

    std::cout << std::endl;
    
    std::cout << "Classes: ";
    for (int i = 0; i < 6; i++)
        if (dataChampion.classAttributes [i])
            std::cout << classesStr[i] << " ";
    std::cout << std::endl;
}

void Champions::storageChampion() {
    FILE *dataFile = fopen("E:/Clion Projects/untitled/saveChampions.sav", "ab");
    fwrite(&dataChampion, sizeof(dataChampion), 1, dataFile);
    fclose(dataFile);
}

void Champions::loadChampionData(FILE* dataFile) {
    fread(&dataChampion, sizeof(dataChampion), 1, dataFile);
}