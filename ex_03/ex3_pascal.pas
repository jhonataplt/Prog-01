{ Leia SOMENTE um número inteiro e imprima uma mensagem contendo }{ o número e um texto: PAR, se o número lido for divisível por 2} 
{ ou exclusivo IMPAR, se o número lido não for divisível por 2. }

Program ex3_pascal;
    { Declaração de Variáveis }
    var num: integer;

    Begin    
        { Entrada }
        write ('Insert a number here: ');
            read (num);
        { Processamento + Saída }
        if (num mod 2 <> 0) then
            write (num, ' IMPAR')
                else
                    write (num, ' PAR');
    End.