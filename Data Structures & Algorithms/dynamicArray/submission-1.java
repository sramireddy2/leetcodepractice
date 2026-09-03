class DynamicArray {

    private int arr[];
    private int length;
    private int capacity;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.arr = new int[this.capacity];
        this.length = 0;
    }

    public int get(int i) {
        if(i >= this.length){
            throw new IllegalArgumentException("Index too large.");
        }
        return this.arr[i];
    }

    public void set(int i, int n) {
        if(i >= this.length){
            throw new IllegalArgumentException("Index too large.");
        }
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if(this.capacity == this.length){
            resize();
        }
        this.arr[this.length] = n;
        this.length += 1;
    }

    public int popback() {
        if (this.length == 0){
            throw new IndexOutOfBoundsException();
        }
        this.length -= 1;
        return this.arr[this.length];
    }

    private void resize() {
        this.capacity *= 2;
        int newarr[] = new int[this.capacity];
        for(int i = 0; i < this.length; i++){
            newarr[i] = this.arr[i];
        }
        this.arr = newarr;
    }

    public int getSize() {
        return this.length;
    }

    public int getCapacity() {
        return this.capacity;
    }   
}
