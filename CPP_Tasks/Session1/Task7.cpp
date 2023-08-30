#include <iostream>
#include <bitset>

int main() {
    // Convert binary to decimal
    std::bitset<8> binaryNumber("10101010");
    unsigned long decimalNumber = binaryNumber.to_ulong();
    std::cout << "Binary: " << binaryNumber << " => Decimal: " << decimalNumber << std::endl;

    // Convert decimal to binary
    unsigned long decimalValue = 170;
    std::bitset<8> binaryValue(decimalValue);
    std::cout << "Decimal: " << decimalValue << " => Binary: " << binaryValue << std::endl;

    return 0;
}