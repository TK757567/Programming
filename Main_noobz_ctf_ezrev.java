public class Main {
    public static void main(String[] strArr) {
        int[] array = new int[]{130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115};

        for (int i2 = 0; i2 <= array.length / 2 - 1; i2++) {
            if (i2 % 2 == 0) {
                int temp1 = array[i2];
                int temp2 = array[(array.length - 1-i2)];
                array[i2] = (char) (temp2 + 10);
                array[(array.length - 1) - i2] = (char) (temp1 - 20);
            } else {
                array[i2] = (char) (array[i2] - 30);
            }
        }
        
        for (int i = array.length - 1; i >= 0; i--) {
            if (i % 2 == 0) {
                array[i] = (char) (array[i] ^ 19);
            } else {
                array[i] = (char) (array[i] ^ 55);
            }
        }
        
        String originalString = new String(array, 0, array.length);
        
        System.out.println(originalString);
    }
    
}
