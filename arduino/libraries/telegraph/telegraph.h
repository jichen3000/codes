#ifndef __TELEGRAPH_H__
#define __TELEGRAPH_H__

typedef void (* OutputSymbolFunction)(const int length);
class Telegraph {
public:
    Telegraph(const int dit_length);
    void send_message(const char* message);
    void subscribe_output(const OutputSymbolFunction output_symbol_function);

private:
    void dit();
    void dah();
    void output_code(const char* code);
    void output_symbol(const int length);

    int _output_pin;
    int _dit_length;
    int _dah_length;
    OutputSymbolFunction _output_symbol_functions[10];
    int _output_symbol_function_size;
};

#endif