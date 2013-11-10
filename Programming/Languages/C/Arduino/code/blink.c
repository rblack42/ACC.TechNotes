#include <avr/io.h>
#include <util/delay.h>

#define LED_ON          (PORTD |= (1<<6))
#define LED_OFF         (PORTD &= ~(1<<6))

#define LED_CONFIG      (DDRD |= (1<<6))
#define CPU_PRESCALE(n) (CLKPR = 0x80, CLKPR = (n))

int main(void) {

    CPU_PRESCALE(0);
    LED_CONFIG;
    LED_OFF;

    while(1){
        LED_ON;
        _delay_ms(500);
        LED_OFF;
        _delay_ms(500);
    }
}
