// You can print the values to stdout for debugging
public class test{
    public static int[] sortArray( int arr[] ){
        int x = 0 , y = 0 , n = arr.length;
        for( x = 0 ; x < n-1 ; x ++ ){
            int index_of_min = x;
            for( y = x+1 ; y < n ; y ++ ){
                if(arr[index_of_min]>arr[x]){
                    index_of_min = y;
                }
            }
            int temp = arr[x];
            arr[x] = arr[index_of_min];
            arr[index_of_min] = temp;
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{3,6,4,1,9,7};
        sortArray(arr);
        System.out.println(arr);
    }
}

