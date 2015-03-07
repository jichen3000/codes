// TemplateVector - a simple templatized vector class 
template <class T>
class TemplateVector
{
public:
    TemplateVector(int nArraySize)
    {
        // store off the number of elements 
        nSize = nArraySize;
        array = new T[nArraySize];
        reset();
    }
    int size() { return nWriteIndex; }
    void reset() { nWriteIndex = 0; nReadIndex = 0; } 
    void add(const T& object)
    {
        if (nWriteIndex < nSize)
        {
            array[nWriteIndex++] = object;
        } 
    }
    T& get()
    {
        return array[nReadIndex++];
    }
protected:
    int nSize;
    int nWriteIndex; int nReadIndex; T* array;
};