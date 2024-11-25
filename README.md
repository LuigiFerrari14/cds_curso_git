# Curso de Git
Este repositório foi criado para hospedar o esqueleto do projeto que será utilizado para explicar e ensinar o uso básico do Git dentro da Comunidade DS



git

git status
git add . 
git commit -m "Comentario"
git commit -m "Comentario" -- amend (pequena mudança/alterar mensagem do ultimo)


git log --oneline

git log -p -numero (ver oq foi alterado) numero=do atual até quantos atras?

git diff <código do mais atual que quer ver > <código mais antigo que quer ver> o que mudou


git rebase -i HEAD~<n> (reestruturar ou reescrever todo histórico local)

git reset --mixed <codigo> (ex, você fez 4 commits, que pode resumir em 1. Você usa o reset --mixed para que o head seja o <código> e o restante fica salvo você poderá fazer um novo commit com todas mudanças juntas


git reset --hard <codigo> (mesma coisa que o de cima, mas apaga tudo até o código que colocou, usa quando tem algum bug e quer apagar tudo até x commit)

git restore <file> (Caso tenha apagado sem querer um arquivo e ainda não tenha commitado)

git reset mixed <codigo> (Caso tenha apagado sem querer um arquivo e tenha dado commitado, você pode voltar para versão anterior e recuperar usando o restore)




GitHub online
 - Cadastro
git remote add origin <link>

git push -u origin main


git remote -v (Ver se funcionou e o nome)
git push <nome> <main> (nome normalmente é = origin // Serve para enviar as atualizações para o GitHub online)


git clone <link> (clonar/fazer download de um projeto)

git fetch ( serve para atualizar o repositório local com as alterações mais recentes do repositório remoto )

git pull (pegar atualizações feitas pelo time, download)


git branch <nome> (Criar nova branch)

git branch (Ver branchs)

git checkout <nome da branch> (alterar de branch a outra) (move o head para o ultimo commit da branch)
git checkout -b <nome da branch> (Cria uma nova branch e move o head para a criada)


git merge <branch>
