
public class Bubblsort {

	public static void main(String[] args) {
		int[] i = {2,4,35,67,5,4,1};
		
		bubbleSort(i);
		for(int n : i){
			System.out.println(n);
		}
		
	}
	public static int[] bubbleSort(int[] array){

        int l = array.length;

        for(int i = 0; i<l; i++){
            for(int j = i+1; j<l; j++){

                if (array[i] > array[j]){
                    int x = array[i];
                    array[i] = array[j];
                    array[j] = x;
                }

            }
        }

        return array;
    }

}
