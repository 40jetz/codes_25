#include <stdio.h>


int main(void)
{


    int myNum ;
    
    
    scanf("%d", &myNum);
    printf("Your number is: %d \n" , myNum );

    // %d , %i , $li , %c , %s

    if (myNum <= 20 ){
        printf("Ya num less than 20");
    }
    
    else if (myNum >= 20){
        printf("Ya num greater than 20");
    }

    else {
        printf("shit");
    }

    
}