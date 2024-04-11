#include <iostream>
#include <string>

using namespace std;

int main() {
    
    string nome_completo, nome, sobrenome;

    cout << "Digite seu nome e sobrenome: ";
    getline(cin, nome_completo);

    size_t pos = nome_completo.find_last_of(' ');

    nome = nome_completo.substr(0, pos);
    sobrenome = nome_completo.substr(pos + 1);

      cout << sobrenome << ", " << nome[0] << nome[nome.length() - 1] << endl;

    return 0;
}
