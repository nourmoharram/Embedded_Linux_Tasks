from jinja2 import Template

# Template for the  Register configurations
c_template = Template("""
#include <avr/io.h>

void Init_PortA_DIR() {
    // Configure DDRAM 8-bit register
    DDRA = 0b{{ configure_ddram }};
}
""")

def generate_c_code(configure_ddram):
    # Render the template with the provided configuration by replacing the placeholder with the actual value
    c_code = c_template.render(configure_ddram=configure_ddram)
    return c_code

def main():
    # Get user configurations
    pin_count = int(input("Enter the number of pins: "))
    configurations = []

    for _ in range(pin_count):
        pin_number = input("Enter pin number: ")
        is_input = input("Is pin an input? (y/n): ").lower()

        # Generate configuration based on user input
        if is_input == "y":
            configure_ddram = "0"
        else:
            configure_ddram ="1"
        configurations.append(configure_ddram)

    # Generate the C code for the Init_PORTA_DIR function
    init_port_a_code = generate_c_code("".join(configurations))

    # Write the generated code to a Configuration.c file
    with open('Configuration.c', 'w') as c_file:
        c_file.write(init_port_a_code)

    print("C code generated and written to 'Configuration.c'")

if __name__ == "__main__":
    main()
