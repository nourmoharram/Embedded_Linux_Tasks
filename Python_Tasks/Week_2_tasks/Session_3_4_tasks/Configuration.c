
#include <avr/io.h>

void Init_PortA_DIR() {
    // Configure DDRAM 8-bit register
    DDRA = 0b01010101;
}