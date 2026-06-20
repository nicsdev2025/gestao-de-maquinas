# gestao-de-maquinas

Criei esse sistema para gerenciar e controlar o uso de máquinas desktops onde eu trabalho.
Percebi que faltava um sistema para verificação, então, para não ter que usar o excel, resolvi criar esse sistema.

Qual o funcionamento desse CRUD:
    Ele adiciona os dados obtidos no terminal do vscode, e manda diretamente pro Dbeaver, na qual fiz a conexão com o SGBD PostgreSQL.
    Altera os dados contidos nas tabelas. De forma selecionada, o usuário pode escolher os dados que ele quer fazer a atualização dentro do terminal, o programa pede os dados e enquanto não for satisfeito, ele continua pedindo os dados certos. 
    Ele também executa a exclusão de dados. A partir do ID (que é gerado automaticamente no Banco de Dados e mostrado no terminal do Vscode), o usuário escolhe o ID da coluna na qual ele quer fazer a exclusão, e logo em seguida é executado o comando.
    Usei a linguagem Python para escrever o código, e usei o paradigma de Programação Orientada a Objetos para estruturar o código que tinha feito anteriormente.

