template< class T1 >
void p(const T1 msg1){
    std::cout << msg1 << std::endl;
}
template< class T1, class T2>
void p(const T1 msg1, const T2 msg2){
    std::cout << msg1 << " " << msg2 << std::endl;
}
template< class T1, class T2, class T3>
void p(const T1 msg1, const T2 msg2, const T3 msg3){
    std::cout << msg1 << " " << msg2 << " " << msg3 << std::endl;
}
template< class T1, class T2, class T3, class T4>
void p(const T1 msg1, const T2 msg2, const T3 msg3, const T4 msg4){
    std::cout << msg1 << " " << msg2 << " " << msg3 << " " << msg4 << std::endl;
}


int main(){
    int upper = 5;
    int lower = 0;
    int count = 100000;
    p("RAND_MAX:",RAND_MAX);
    for (size_t j = 0; j < count; j++) {
        int rand_v = rand();
        int i = (int) ((double)rand_v / RAND_MAX * (upper - lower - 1)) + lower;
        if (i>lower && i>=(upper - lower - 1))
            p(rand_v,i);
    }
}
