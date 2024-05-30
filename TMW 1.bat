@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title TMW: Novo Mundo
color 0A
if "%1" neq "" ( goto %1)

set /a vida=15
set /a defesa=5
set /a ataque=5
set /a energia=5

:Menu
cls
echo.
echo ------------------------------------
echo.
echo ┏┳┓┓┏┏┓  ┳┳┓┏┓┳┓┏┳┓┏┓┓   ┓ ┏┏┓┳┓┓ ┳┓
echo  ┃ ┣┫┣   ┃┃┃┣ ┃┃ ┃ ┣┫┃   ┃┃┃┃┃┣┫┃ ┃┃
echo  ┻ ┛┗┗┛  ┛ ┗┗┛┛┗ ┻ ┛┗┗┛  ┗┻┛┗┛┛┗┗┛┻┛
echo.
echo ------------------------------------
echo.
echo [1] Iniciar o Jogo
echo [2] Sair
echo.
set /p resposta=Escolha uma opção e pressione ENTER: 
if %resposta%==1 goto Iniciar
if %resposta%==2 goto Sair

:Sair
cls
echo Obrigado por jogar!
pause
exit /b

:Iniciar
cls
echo.
echo "Houve uma época em que a existência de energia não era algo conhecido.
echo Quando isso mudou, a humanidade foi tomada por organizações e pessoas arrogantes.
echo A influência que exerciam sobre a sociedade causou efeitos inimagináveis.
echo Mal sabiam eles do destino que seriam forçados a encarar.
echo.
pause
cls
echo.
echo Esse era o fim dos tempos.
echo.
echo Não havia nenhuma chance de sobrevivência.
echo.
pause
cls
color 04
echo.
echo E foi assim que você morreu."
echo.
pause
cls
echo.
echo Você desperta em um mundo que não te pertence.
echo O solo sob seus pés berra e treme sem fim.
echo O céu acima parece puxá-lo com violência.
echo E o ar ao seu redor o pressiona para baixo,
echo tentando abrir caminho para dentro.
echo.
pause
cls
color 09
echo.
echo Este é o planeta Terra.
echo Um mundo cruel que nunca deveria ter existido.
echo O ano é 2052, um futuro distópico onde a tecnologia
echo já se tornou algo único com a humanidade.
echo.
pause
color 0A
goto raca

:raca
cls
echo.
echo ------------------------
echo     Escolha sua raça
echo ------------------------
echo.
echo [1] Humano
echo [2] Androide
echo [3] Cyborg
echo [4] Ultra-humano
echo.

set /p resp1=Resposta: 
if !resp1!==1 (
    set raca=humano
    set bonus=+5 HP -5 DEF
    set bonus1= !vida! + 5
    set bonus2= !defesa! - 5
) else if !resp1!==2 (
    set raca=androide
    set bonus=+5 DEF -5 HP
    set bonus1= !defesa! + 5
    set bonus2= !vida! - 5
) else if !resp1!==3 (
    set raca=cyborg
    set bonus=+5 ATQ -5 NRG
    set bonus1= !ataque! + 5
    set bonus2= !energia! - 5
) else if  !resp1!==4 (
    set raca=ultra-humano
    set bonus=+5 NRG -5 ATQ
    set bonus1= !energia! + 5
    set bonus2= !ataque! - 5
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto raca
)
goto origem

:origem
cls
echo.
echo Você é um !raca!.
echo.
if !raca! equ humano (
    echo - Humanos são seres feitos de fluidos, carne e ossos.
    echo - Sua composição é de 99%% oxigênio, carbono, hidrogênio, cálcio e fósforo.
    echo - Eles possuem olhos, ouvidos, narinas e boca, além do cérebro para pensar e sentir.
    echo - Seu cérebro é composto por neurônios conectados entre si, capazes de processar informações e pensamentos.
    echo - Seus membros são formados por tecidos e ossos, permitindo várias categorias de movimento.
    echo - Eles nascem de uma mãe e pai biológicos, por meio de reprodução sexuada.
    echo.
    echo Bônus da raça: !bonus!
) else if !raca! equ androide (
    echo - Androides são seres feitos de titânio vandal, ferro de detroid e nano liga de cromo-bário.
    echo - Sua composição é de 99%% silício, cromo-bário, cobre, ferro e titânio.
    echo - Eles não possuem olhos, ouvidos, narinas ou boca. Nem mesmo um cérebro para pensar ou sentir.
    echo - Seu processador é composto por circuitos conectados entre si, capazes de processar dados e variáveis.
    echo - Seus membros são formados por ligas metálicas e tecidos emborrachados, permitindo várias categorias de movimento.
    echo - Eles são construídos por uma fábrica, sendo incapazes de se reproduzir.
    echo.
    echo Bônus da raça: !bonus!
) else if !raca! equ cyborg (
    echo - Cyborgs são seres feitos de fluidos, carne, ossos, borracha e metais.
    echo - Sua composição é imprecisa e variável, dependendo bastante do grau de modificação.
    echo - Eles podem ou não possuir olhos, ouvidos, narinas e boca, além de um cérebro ou processador.
    echo - Seus membros mecânicos são conhecidos como "Cromos", permitindo o aumento das capacidades físicas e/ou mentais.
    echo - Eles nascem da mesma forma que humanos, mas são modificados por meio de cirurgias e implantes.
    echo - Podem se modificar até o limite de seus corpos biológicos.
    echo.
    echo Bônus da raça: !bonus!
) else if !raca! equ ultra-humano (
    echo - Ultra-humanos são seres feitos de fluidos, carne e ossos.
    echo - Sua composição é de 99%% oxigênio, carbono, hidrogênio, cálcio e fósforo.
    echo - Eles possuem olhos, ouvidos, narinas e boca, além do cérebro para pensar e sentir.
    echo - Seu cérebro é composto por neurônios conectados entre si, capazes de processar informações e pensamentos.
    echo - Seus membros são formados por tecidos e ossos, permitindo várias categorias de movimento.
    echo - Eles nascem de uma mãe e pai biológicos, por meio de reprodução sexuada.
    echo - O que os diferencia dos humanos é a capacidade de manipular energia, permitindo o uso de habilidades especiais.
    echo.
    echo Bônus da raça: !bonus!
)
echo.
echo Tem certeza de sua escolha? [S/N]
set /p resposta=Escolha uma opção e pressione ENTER: 
if !resposta!==s (
    goto classe
) else if !resposta!==n (
    goto raca
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto origem
)

:classe
cls
echo.
echo -----------------------------
echo Escolha seu estilo de combate
echo -----------------------------
echo.
echo [1] Corpo a corpo
echo [2] Armas corpo a corpo
echo [3] Magia arcana
echo [4] Armas de fogo
echo [5] Cromos
echo.

set /p resp2=Resposta: 
if !resp2!==1 (
    set combat=combate corpo a corpo
    set combat_tipo=fisico1
) else if !resp2!==2 (
    set combat=armas corpo a corpo
    set combat_tipo=fisico2
) else if !resp2!==3 (
    set combat=magia arcana
    set combat_tipo=magia
) else if  !resp2!==4 (
    set combat=armas de fogo
    set combat_tipo=fogo
) else if  !resp2!==5 (
    set combat=cromos
    set combat_tipo=cromos
) else (
    echo Entrada Invalida, tente novamente.
    pause
    goto raca
)
goto origem2

:origem2
cls
echo.
echo Você é um !raca! que luta utilizando !combat!.
echo.
if !combat_tipo! equ fisico1 (
    echo - "Combate corpo a corpo" é um estilo de combate que envolve o uso de técnicas de luta desarmada.
    echo - Ele é baseado em golpes físicos, como socos, chutes, cotoveladas e joelhadas.
    echo - É um estilo que exige força, agilidade e resistência física.
    echo.
    echo Exemplos de armas: Luvas, botas, armaduras, etc.
) else if !combat_tipo! equ fisico2 (
    echo - "Armas corpo a corpo" é um estilo de combate que envolve o uso de armas corpo a corpo.
    echo - Ele é baseado em ataques à curta distância, como cortes, estocadas e esquivas.
    echo - É um estilo que exige força, agilidade e resistência física.
    echo.
    echo Exemplos de armas: Espadas, machados, lanças, etc.
) else if !combat_tipo! equ magia (
    echo - "Magia arcana" é um estilo de combate que envolve o uso de energia e encantamentos.
    echo - Ele é baseado em "skills" energéticas, como bolas de fogo, raios e escudos espectrais.
    echo - Pode ser usado à curta e longa distância, dependendo da escolha do usuário.
    echo - É um estilo que exige concentração, sabedoria e resistência mental.
    echo.
    echo Exemplos de armas: Amuletos, artefatos, pergaminhos, etc.
) else if !combat_tipo! equ fogo (
    echo - "Armas de fogo" é um estilo de combate que envolve o uso de armas de fogo.
    echo - Ele é baseado em ataques à longa distância, como tiros, granadas e explosões.
    echo - É um estilo que exige precisão, agilidade e sabedoria.
    echo.
    echo Exemplos de armas: Pistolas, rifles, metralhadoras, etc.
) else if !combat_tipo! equ cromos (
    echo - "Cromos" é um estilo de combate que envolve o uso de implantes cibernéticos.
    echo - Ele é baseado em ataques à curta e longa distância, como socos, tiros e explosões.
    echo - É um estilo que exige força, concentração e agilidade.
    echo.
    echo Exemplos de armas: Braços mecânicos, pernas mecânicas, olhos cibernéticos, etc.
)
echo.
echo Tem certeza de sua escolha? [S/N]
set /p resposta=Escolha uma opção e pressione ENTER: 
if !resposta!==s (
    goto historia
) else if !resposta!==n (
    goto classe
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto origem2
)

:historia
cls
echo.
echo -----------------------------
echo      Escolha sua origem
echo -----------------------------
echo.
echo [1] Cidade
echo [2] Floresta
echo [3] Deserto
echo [4] Montanha
echo [5] Mar
echo.
set /p resp3=Resposta: 
if !resp3!==1 (
    set origem=cidade
) else if !resp3!==2 (
    set origem=floresta
) else if !resp3!==3 (
    set origem=deserto
) else if  !resp3!==4 (
    set origem=montanha
) else if  !resp3!==5 (
    set origem=mar
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto historia
)
goto origem3

:origem3
cls
echo.
if "!origem!"=="floresta" set preposicao=da
if "!origem!"=="cidade" set preposicao=da
if "!origem!"=="montanha" set preposicao=da
if "!origem!"=="deserto" set preposicao=do
if "!origem!"=="mar" set preposicao=do
echo Você é um !raca! que luta utilizando !combat! e vem !preposicao! !origem!.
echo.
if !origem! equ cidade (
    echo Você nasceu e cresceu em uma cidade pouco movimentada chamada "Mydensgate".
    echo Ela é conhecida por sua atmosfera sombria e poluída, onde a luz do sol raramente é vista.
    echo A população é composta por humanos e cyborgs que vivem entre dois mundos, a riqueza e a pobreza.
    echo A cidade é governada por uma corporação chamada "Infinity", que controla a economia e a política.
    echo.
    echo Como qualquer outro cidadão, seu sonho sempre foi se tornar um herói profissional.
    echo Você treinou e estudou por anos, mas algo o impediu de alcançar seu objetivo...
) else if !origem! equ floresta (
    echo Você nasceu e cresceu em uma floresta densa e misteriosa chamada "Eldergrove".
    echo Ela é conhecida por sua atmosfera calma e pacífica, onde a luz do sol brilha entre os vãos das árvores.
    echo A população é composta por humanos e animais que vivem em harmonia com a natureza.
    echo A floresta é governada pelos "Scroll Travellers", que protegem a lendária árvore especial.
    echo.
    echo Como um membro dos Scroll Travellers, seu dever sempre foi proteger a árvore e os habitantes da floresta.
    echo Você treinou e estudou por anos, mas algo o impediu de alcançar seu objetivo...
) else if !origem! equ deserto (
    echo Você nasceu e cresceu em um deserto vasto e inóspito chamado "Pharr Cânion".
    echo Ele é conhecido por sua atmosfera quente e seca, onde a luz do sol queima a pele e os olhos.
    echo A população é composta por humanos e animais que vivem em busca de água e comida.
    echo O deserto é governado pelos "Kobra", que controla o comércio e a religião.
    echo.
    echo Como qualquer outro habitante dos ermos, seu sonho sempre foi tirar sua família da pobreza.
    echo Você treinou e estudou por anos, mas algo o impediu de alcançar seu objetivo...
) else if !origem! equ montanha (
    echo Você nasceu e cresceu em uma montanha alta e perigosa chamada "Pináculo da Ascensão".
    echo Ela é conhecida por sua atmosfera fria e ventosa, onde a luz do sol brilha entre os picos das montanhas.
    echo A população é composta por humanos e cyborgs que vivem em busca de alcançar a paz interior.
    echo A montanha é governada pelos "Eremitas", que ensinam sobre as artes do eremitismo.
    echo.
    echo Como um membro dos Eremitas, seu dever sempre foi alcançar a paz interior e a iluminação espiritual.
    echo Você treinou e estudou por anos, mas algo o impediu de alcançar seu objetivo...
) else if !origem! equ mar (
    echo Você nasceu e cresceu em um mar turbulento chamado erroneamente de "Oceano de Prata".
    echo Ele é conhecido por sua atmosfera úmida e tempestuosa, onde a luz do sol nem sempre brilha.
    echo A população é composta por humanos e cyborgs piratas que vivem do pouco que conseguem roubar.
    echo O mar é governado pelos "Corsários", que controlam o comércio e a pirataria.
    echo.
    echo Com a vida como ela é, seu sonho sempre foi encontrar um tesouro lendário e se tornar rico.
    echo Você treinou e roubou por anos, mas algo o impediu de alcançar seu objetivo...
)
echo.
echo Tem certeza de sua escolha? [S/N]
set /p resposta=Escolha uma opção e pressione ENTER: 
if !resposta!==s (
    goto nome
) else if !resposta!==n (
    goto historia
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto origem3
)

:nome
cls
echo.
echo ------------------------------
echo    Digite seu primeiro nome
echo ------------------------------
echo.
set /p nome=Nome: 
echo.
echo Tem certeza de sua escolha? [S/N]
set /p resposta=Escolha uma opção e pressione ENTER: 
if !resposta! equ s (
    goto finalizarc
) else if !resposta! equ n (
    goto nome
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto nome
)

:finalizarc
cls
echo.
echo Você é um !raca! que luta utilizando !combat! e vem !preposicao! !origem!. Seu nome é !nome!.
echo.
echo No mundo atual, o conceito de gênero e sexualidade é algo ultrapassado e visto como preconceituoso.
echo Por isso, não é necessário escolher um gênero ou sexualidade que te definam.
echo Você é livre para ser quem quiser, sem julgamentos ou limitações.
echo Seu corpo é seu templo, sua mente é seu santuário e sua alma é seu refúgio.
echo Todos são considerados iguais perante a lei e a sociedade, sem exceções ou privilégios.
echo.
echo Contudo, sem a existência de diferenças, a vida se tornou monótona e sem sentido.
echo.
pause
cls
echo.
echo Sempre houveram rumores em circulação sobre os ideais desconhecidos da Corporação Infinity.
echo Ela sempre foi vista como uma organização benevolente e justa, perfeita até demais.
echo Mas, como qualquer outra organização, possui segredos e mistérios que ninguém conhece.
echo Alguns dizem que ela é responsável pela destruição das ideias de indivíduo e personalidade.
echo Outros falam que ela busca o controle absoluto sobre a humanidade, sem exceções ou limites.
echo.
echo Quem sabe esses murmúrios não estejam certos...
echo Nesse caso, nós seriamos apenas figurantes em um gigantesco teatro.
echo.
pause
cls
echo.
echo As coisas começam a mudar quando percebemos que a Infinity não é a única movendo os pauzinhos.
echo Organizações secretas por todo o globo estão se movendo, tentando alcançar seus objetivos.
echo Logo, uma terceira guerra mundial irá começar entre todos os países.
echo E, como sempre, a população será a mais afetada por essa guerra.
echo.
echo Não há ninguém que possa impedir isso de acontecer.
echo O futuro já está completamente comprometido.
echo.
pause
goto inicio

:inicio
cls
echo.
color 06
if !raca! equ humano (
    echo Você acorda após uma noite de sono mal dormida.
    echo O sol brilha através da janela, iluminando seu rosto com uma luz suave.
    echo.
    echo Você se levanta da cama e se espreguiça, sentindo o corpo dolorido e cansado.
    echo O dia anterior foi longo e estressante, mas esquecível, como todos os outros.
    echo.
    pause
    cls
    echo.
    echo Algo chama sua atenção vindo do âmago de sua essência.
    echo Um amálgama de sentimentos indesejáveis, diferentes de medo, raiva ou tristeza.
    echo Seria difícil deduzir o que é, mas é certo o desconforto que isso causa.
    echo.
    echo [1] Ignorar
    echo [2] Investigar
    echo.
    set /p opcao1=Escolha uma opção e pressione ENTER: 
    if !opcao1! equ 1 (
        goto ignorar
    ) else if !opcao1! equ 2 (
        goto investigar
    ) else (
        echo Entrada Inválida, tente novamente.
        pause
        goto inicio
    )
) else if !raca! equ ultra-humano (
    echo Você acorda após uma noite de sono mal dormida.
    echo O sol brilha através da janela, iluminando seu rosto com uma luz suave.
    echo.
    echo Você se levanta da cama e se espreguiça, sentindo o corpo dolorido e cansado.
    echo O dia anterior foi longo e estressante, mas esquecível, como todos os outros.
    echo.
    pause
    cls
    echo.
    echo Algo chama sua atenção vindo do âmago de sua essência.
    echo Um amálgama de sentimentos indesejáveis, diferentes de medo, raiva ou tristeza.
    echo Seria difícil deduzir o que é, mas é certo o desconforto que isso causa.
    echo.
    echo [1] Ignorar
    echo [2] Investigar
    echo.
    set /p opcao1=Escolha uma opção e pressione ENTER: 
    if !opcao1! equ 1 (
        goto ignorar
    ) else if !opcao1! equ 2 (
        goto investigar
    ) else (
        echo Entrada Inválida, tente novamente.
        pause
        goto inicio
    )
) else if !raca! equ cyborg (
    echo Você acorda após uma noite de sono mal dormida.
    echo O sol brilha através da janela, iluminando seu rosto com uma luz suave.
    echo.
    echo Você se levanta da cama e se espreguiça, sentindo o peso dos cromos empurrando sua carne.
    echo O dia anterior foi longo e estressante, mas esquecível, como todos os outros.
    echo.
    pause
    cls
    echo.
    echo Algo chama sua atenção vindo do âmago de sua essência.
    echo Um amálgama de sentimentos indesejáveis, diferentes de medo, raiva ou tristeza.
    echo Seria difícil deduzir o que é, mas é certo o desconforto que isso causa.
    echo.
    echo [1] Ignorar
    echo [2] Investigar
    echo.
    set /p opcao1=Escolha uma opção e pressione ENTER: 
    if !opcao1! equ 1 (
        goto ignorar
    ) else if !opcao1! equ 2 (
        goto investigar
    ) else (
        echo Entrada Inválida, tente novamente.
        pause
        goto inicio
    )
) else if !raca! equ androide (
    echo Você é reativado após recarregar o núcleo por uma noite inteira.
    echo O sol brilha através da janela, iluminando seu rosto com uma luz suave.
    echo.
    echo Você desconecta os cabos de energia de seu corpo, permitindo que possa movimentar as pernas.
    echo Ao ficar de pé, os sensores indicam que as placas do processador estão 27.2%% inoperantes.
    echo O dia anterior foi longo, excedendo o número de variáveis que seu corpo é capaz de computar.
    echo Mesmo assim, não é como se essa fosse a primeira vez que isso acontece.
    echo.
    pause
    cls
    echo.
    echo Algo chama sua atenção vindo do âmago de sua essência.
    echo Um amálgama de dados indesejáveis, diferentes dos protocolos já reconhecidos.
    echo Seria difícil deduzir o que é, mas é certo o desconforto que isso causa.
    echo.
    echo [1] Ignorar
    echo [2] Investigar
    echo.
    set /p opcao1=Escolha uma opção e pressione ENTER: 
    if !opcao1! equ 1 (
        goto ignorar2
    ) else if !opcao1! equ 2 (
        goto investigar2
    ) else (
        echo Entrada Inválida, tente novamente.
        pause
        goto inicio
    )
)

:ignorar2
cls
echo.
echo Você decide ignorar os dados e seguir com sua rotina diária.
echo Seus protocolos são muitos e seu tempo é pouco, não há espaço para distrações.
echo Se algo tão ínfimo pudesse te afetar, então você não seria digno de ter o dom da existência.
echo.
pause
cls
echo.
echo Você se arruma e desce as escadas, indo em direção ao banheiro.
echo O espelho reflete sua imagem, mostrando um rosto metálico e sem vida.
echo.
echo [1] Limpar exoesqueleto
echo [2] Trocar fluidos
echo [3] Sair de casa
echo.
set /P opcao2=Escolha uma opção e pressione ENTER:
if !opcao2! equ 1 (
    goto limparexo
) else if !opcao2!==2 (
    goto trocarflu
) else if !opcao2!==3 (
    goto sairdecasa
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto ignorar2
)

:ignorar
cls
echo.
echo Você decide ignorar o sentimento e seguir com sua rotina diária.
echo Suas preocupações são muitas e seu tempo é pouco, não há espaço para distrações.
echo Se algo tão ínfimo pudesse te afetar, então você não seria digno de ter o dom da vida.
echo.
pause
cls
echo.
echo Você se arruma e desce as escadas, indo em direção ao banheiro.
echo O espelho reflete sua imagem, mostrando um rosto cansado e sem vida.
echo.
echo [1] Tomar banho
echo [2] Escovar os dentes
echo [3] Sair de casa
echo.
set /P opcao2=Escolha uma opção e pressione ENTER:
if !opcao2!==1 (
    goto banho
) else if !opcao2!==2 (
    goto escovar
) else if !opcao2!==3 (
    goto sairdecasa
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto ignorar
)

:banho
cls
echo.
echo Você toma um banho quente e relaxante, permitindo que a água leve embora suas preocupações.
echo O vapor preenche o ambiente, criando uma atmosfera úmida e confortável.
echo Tudo parece bem, mas algo ainda te incomoda.
echo.
pause
cls
echo.
echo As memórias do dia anterior parecem distantes e confusas.
echo Você se lembra de ter feito algo importante, mas não consegue se recordar o que é.
echo A sensação de vazio e desespero começa a tomar conta de sua mente.
echo.
pause
cls
echo.
echo Enquanto a água escorre pelo seu corpo, um som estridente ecoa ao longe.
echo Ele parece vir de fora de sua casa, como se alguém estivesse tentando te chamar.
echo As palavras parecem incompreensíveis e profanas, nada faz sentido a esse ponto.
echo.
echo [1] Investigar
echo [2] Sair de casa
echo.
set /P opcao3=Escolha uma opção e pressione ENTER:
if !opcao3!==1 (
    goto investigar4
) else if !opcao3!==2 (
    goto sairdecasa
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto banho
)

:escovar
cls
echo.
echo Você escova os dentes e lava o rosto, tentando se livrar da estranha sensação.
echo A pasta, tingida de azul, toca o interior de sua boca, causando uma pequena ardência.
echo A água, fria e cristalina, escorre pelo seu rosto, levando consigo o sono.
echo Com os dentes e o rosto limpos, o melhor a se fazer é seguir com a rotina.
echo.
echo [1] Tomar banho
echo [2] Sair de casa
echo.
set /P opcao3=Escolha uma opção e pressione ENTER:
if !opcao3!==1 (
    goto banho
) else if !opcao3!==2 (
    goto sairdecasa
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto banho
)

:investigar
cls
echo.
echo Você decide investigar o sentimento e tentar descobrir o que está acontecendo.
echo Não é normal sentir algo assim, ainda mais sem motivo aparente.
echo Mesmo parecendo algo ínfimo, pode vir a se tornar um problema mais tarde.
echo.
pause
cls
echo.
echo Você fecha os olhos e se concentra, tentando descobrir a origem da sensação.
echo Ela parece vir de algum lugar próximo. Uma memória a muito tempo esquecida.
echo Seus pensamentos começam a se emaranhar, formando uma imagem em sua mente.
echo.
pause
cls
echo.
echo Antes que possa ver o que é, a imagem desaparece por culpa de um som estridente ao longe.
echo Você abre os olhos e percebe que o som vem de fora de sua casa.
echo Uma silhueta sombria te observa através da janela.
echo.
echo [1] Investigar
echo [2] Sair de casa
echo.
set /P opcao4=Escolha uma opção e pressione ENTER:
if !opcao4!==1 (
    goto investigar3
) else if !opcao4!==2 (
    goto sairdecasa
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto investigar
)

:investigar2
cls
echo.
echo Você decide investigar os dados e tentar descobrir o que está acontecendo.
echo Seus sensores não costumam falhar, ainda mais sem motivo aparente.
echo Mesmo parecendo algo ínfimo, pode vir a se tornar um problema mais tarde.
echo.
pause
cls
echo.
echo Você envia 45.5%% dos recursos energéticos para o processador.
echo Ele começa a processar os dados, tentando encontrar a origem da incongruência.
echo Ela parece vir de algum lugar próximo. Um protocolo a muito tempo apagado.
echo As variáveis começam a se emaranhar, formando um ácumulo de informações.
echo.
pause
cls
echo.
echo Antes dos resultados, o foco dos sensores é tomado por um som estridente ao longe.
echo Você direciona os sensores pelo quarto, tentando identificar a origem do som.
echo Uma silhueta sombria te observa através da janela.
echo.
echo [1] Investigar
echo [2] Sair de casa
echo.
set /P opcao5=Escolha uma opção e pressione ENTER:
if !opcao5!==1 (
    goto investigar3
) else if !opcao5!==2 (
    goto sairdecasa
) else (
    echo Entrada Inválida, tente novamente.
    pause
    goto investigar2
)

