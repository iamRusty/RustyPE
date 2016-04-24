/********************************************************
 Project Euler 23 - Number spiral diagonals
 
 Goal: Find the sum on the diagonals 1001 x 1001

 Remarks: EZ
********************************************************/
public class ProjectEuler23
{   
    public static void main(String[] args)
    {
        int _DIMENSION_ = 1001;
        long answer;
        answer = getSum(_DIMENSION_);
        System.out.println(answer);
    }
    
    public static long getSum(int dimension)
    {
        int count, count2, temporary_number;
        long sum = 1;
        for (count = 3, temporary_number = 1; count <= dimension; count+=2)
        {
            for(count2 = 1; count2 <= 4; count2++)
            {
                sum += (temporary_number += (count - 1));
            }        
        }
        return sum;
    }    
}