#include "Champions.h"

int main(){
    char nameChampion[NUMCHAMPIONS][20] = {{"Aphelios"},{"Ashe"},{"Caitlyn"},{"Draven"},{"Ezreal"},{"Jhin"},{"Jinx"},
    {"Kai'sa"},{"Kalista"},{"Kog'Maw"},{"Lucian"},{"Miss Fortune"},{"Samira"},{"Senna"},{"Sivir"},{"Tristana"},{"Twitch"},
    {"Varus"},{"Vayne"},{"Xayah"},{"Ahri"},{"Akali"},{"Anivia"},{"Annie"},{"Aurelion Sol"},{"Azir"},{"Cassiopeia"},
    {"Corki"},{"Diana"},{"Ekko"},{"Fizz"},{"Heimerdinger"},{"Irelia"},{"Kassadin"},{"Katarina"},{"LeBlanc"},{"Lissandra"},
    {"Lucian"},{"Lux"},{"Malzahar"},{"Neeko"},{"Orianna"},{"Pantheon"},{"Qiyana"},{"Ryze"},{"Sylas"},{"Syndra"},
    {"Talon"},{"Twisted Fate"},{"Veigar"},{"Viego"},{"Viktor"},{"Vladimir"},{"Xerath"},{"Yasuo"},{"Zed"},{"Ziggs"},
    {"Zoe"},{"Alistar"},{"Bardo"},{"Blitzcrank"},{"Brand"},{"Braum"},{"Galio"},{"Janna"},{"Karma"},{"Leona"},{"Lulu"},
    {"Lux"},{"Maokai"},{"Morgana"},{"Nami"},{"Nautilus"},{"Pyke"},{"Rakan"},{"Rell"},{"Senna"},{"Seraphine"},{"Sett"},
    {"Shaco"},{"Sona"},{"Soraka"},{"Swain"},{"Taric"},{"Thresh"},{"Vel'Koz"},{"Xerath"},{"Yuumi"},{"Zilean"},{"Zyra"},
    {"Aatrox"},{"Camille"},{"Cho'Gath"},{"Darius"},{"Dr. Mundo"},{"Fiora"},{"Gangplank"},{"Garen"},{"Gnar"},{"Gwen"},
    {"Heimerdinger"},{"Illaoi"},{"Irelia"},{"Jax"},{"Jayce"},{"Kayle"},{"Kennen"},{"Kled"},{"Lee Sin"},{"Malphite"},
    {"Mordekaiser"},{"Nasus"},{"Ornn"},{"Quinn"},{"Renekton"},{"Riven"},{"Shen"},{"Singed"},{"Sion"},{"Sylas"},
    {"Tahm Kench"},{"Teemo"},{"Tryndamere"},{"Urgot"},{"Vayne"},{"Wukong"},{"Yasuo"},{"Yone"},{"Yorick"},{"Amumu"},
    {"Diana"},{"Elise"},{"Evelynn"},{"Fiddlesticks"},{"Gragas"},{"Graves"},{"Hecarim"},{"Ivern"},{"Jarvan IV"},
    {"Karthus"},{"Kayn"},{"Kha'Zix"},{"Kindred"},{"Lee Sin"},{"Lillia"},{"Master Yi"},{"Nidalee"},{"Nocturne"},
    {"Nunu e Willump"},{"Olaf"},{"Poppy"},{"Rammus"},{"Rek'Sai"},{"Rengar"},{"Rumble"},{"Sejuani"},{"Shyvana"},
    {"Skarner"},{"Taliyah"},{"Trundle"},{"Udyr"},{"Vi"},{"Volibear"},{"Warwick"},{"Xin Zhao"}, {"Zac"}};
    Champions dataChampion [NUMCHAMPIONS];
    int roleInput, classInput;

    FILE* dataFile;
    dataFile = fopen("saveChampions.sav", "wb");
    fclose(dataFile);
    for (int i = 0; i < NUMCHAMPIONS; i ++){
        dataChampion[i].createChampion(nameChampion[i]);
        dataChampion[i].ShowChampionInfo();
    }

    dataFile = fopen("saveChampions.sav", "rb");
    for (int i = 0; i < NUMCHAMPIONS; i ++){
        dataChampion[i].loadChampionData(dataFile);
        dataChampion[i].ShowChampionInfo();
    }
    fclose(dataFile);



    for (int i = 0; i < 3; i ++){

        dataChampion[i].ShowChampionInfo();
        std::cout << "Insira as funcoes do campeao [-1 para encerrar]: " << std::endl;
        std::cout << "[0] Top Laner" << std::endl << "[1] Jungler" << std::endl << "[2] Mid Laner" << std::endl;
        std::cout << "[3] Ad Carry" << std::endl << "[4] Suporte" << std::endl;
        std::cin >> roleInput;
        while (roleInput >= 0){
            dataChampion[i].addRoleChampion(roleInput);
            std::cin >> roleInput;
        }

        std::cout << "Insira as classes do campeao [-1 para encerrar]:" << std::endl;
        std::cout << "[0] Assassino" << std::endl << "[1] Mago" << std::endl << "[2] Lutador" << std::endl;
        std::cout << "[3] Atirador" << std::endl << "[4] Suporte" << std::endl << "[5] Tanque" << std::endl;
        std::cin >> classInput;
        while (classInput >= 0){
            dataChampion[i].addClassChampion(classInput);
            std::cin >> classInput;
        }
        dataChampion[i].storageChampion();
        dataChampion[i].ShowChampionInfo();
        fflush(dataFile);
    }
    fclose(dataFile);

    dataFile = fopen("saveChampions.sav", "rb");
    for (int i = 0; i < NUMCHAMPIONS; i ++){
        dataChampion[i].loadChampionData(dataFile);
    }
    fclose(dataFile);

    for (int i = 0; i < NUMCHAMPIONS; i ++){
        dataChampion[i].ShowChampionInfo();
    }



    return 0;
}

/*dataFile = fopen("E:/Clion Projects/untitled/saveChampions.sav", "rb");
    for (int i = 0; i < NUMCHAMPIONS; i ++){
        champions[i].loadChampionData(dataFile);
    }
    fclose(dataFile);

    for (int i = 0; i < NUMCHAMPIONS; i ++){
        champions[i].ShowChampionInfo();
    }*/
/*for (int i = 0; i < NUMCHAMPIONS; i ++){
        champions[i].createChampion(nameChampion[i]);
        champions[i].addClassChampion(MARKSMAN);
        champions[i].storageChampion();
        champions[i].ShowChampionInfo();
    }*/