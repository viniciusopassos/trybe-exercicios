### Parte II - Permissões

1. Navegue até a pasta `unix_tests` ;

   _**Resposta**_

   - `cd unix_tests`

2. Rode o comando [ls ](https://linux.die.net/man/1/ls)`-l` e veja quais as permissões dos arquivos;

   _**Resposta**_

   - `total 24
     -rw-rw-r-- 1 developer developer 2073 abr 18 14:13 bunch_of_things.txt
     -rw-rw-r-- 1 developer developer 1842 abr 11 13:59 countries.txt
     -rw-rw-r-- 1 developer developer    0 abr 14 16:56 empty.tbt
     -rw-rw-r-- 1 developer developer    0 abr 14 16:56 empty.txt
     -rw-rw-r-- 1 developer developer  231 abr 18 14:03 phrases2.txt
     -rw-rw-r-- 1 developer developer  243 abr 18 13:37 phrases.txt
     -rw-rw-r-- 1 developer developer   57 abr 15 07:12 skills2.txt
     -rw-rw-r-- 1 developer developer   19 abr 18 13:27 top_skills.txt`

3. Mude a permissão do arquivo `bunch_of_things.txt` para que todos os usuários possam ter acesso à leitura e escrita, e verifique se está correto com o comando `ls -l` ;

   > Resultado esperado: `-rw-rw-rw- 1 ana ana 1860 ago 13 11:39 bunch_of_things.txt`

   _**Resposta**_

   - `chmod 666 bunch_of_things.txt `

4. Tire a permissão de escrita do arquivo `bunch_of_things.txt` para todos os usuários, verifique se está correto com o comando `ls -l` ;

   > Resultado esperado: `-r--r--r-- 1 ana ana 1860 ago 13 11:39 bunch_of_things.txt`

   _**Resposta**_

   - ` chmod 444 bunch_of_things.txt`

5. Volte à permissão do arquivo `bunch_of_things.txt` para a listada inicialmente utilizando o comando `chmod 644 bunch_of_things.txt` .

   > Resultado esperado: `-rw-r--r-- 1 ana ana 1860 ago 13 11:39 bunch_of_things.txt`

   _**Resposta**_ 

   -  `chmod 644 bunch_of_things.txt`

