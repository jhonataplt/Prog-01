Program ex3_pascal;
    {
    ! Variable Declaration }
    var num: integer;

    Begin    
        {
        !Input }
        write ('Insert a number here: ');
            read (num);
        {
        ! Data Processment + Output }
        if (num mod 2 <> 0) then
            write (num, ' IMPAR')
                else
                    write (num, ' PAR');
    End.