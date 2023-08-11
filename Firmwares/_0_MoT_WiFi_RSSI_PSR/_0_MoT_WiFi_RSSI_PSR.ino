
#include "Bibliotecas.h"

#ifndef STASSID

//+++++++COLOCAR A REDE WiFi QUE SERÁ UTILIZADA COM SSID E PASSWORD
// REDE TP-LINK
//#define ssid "TP-LINK_B332EC"           // Nome da Rede TP-LINK_B332EC
//#define password  "EDB332EC"        // Senha da Rede TP-LINK_B332EC

// REDE INF505 - ESSA REDE É SÓ PARA TESTE E NÃO TEM SENHA
#define ssid "INF505"           // Nome da Rede INF505
#define password  ""        // Rede INF505 não tem senha
// IP atribuido pelo AP INF505  192.168.0.2


#endif
unsigned int localPort = 8888;      // Porta na qual o servidor ficará escutando
String newHostname = "SENSOR001";   // Nome do Host na rede

void setup() {
Phy_initialize(); // Inicializa a camada Física
Mac_initialize(); // Inicializa a camada de Controle de Acesso ao Meio
Net_initialize(); // Inicializa a camada de Rede
Transp_initialize(); // Inicializa a camada de Transporte
App_initialize(); // Inicializa a camada de Aplicação
}

void loop() {
Phy_receive(); 
}
