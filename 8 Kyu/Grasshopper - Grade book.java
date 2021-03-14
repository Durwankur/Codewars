public class GrassHopper {

    public static char getGrade(int s1, int s2, int s3) {
        int m = (s1+s2+s3)/3;
      if(m>=90 && m<=100) return 'A';
      else if(m>=80 && m<90) return 'B';
      else if(m>=70 && m<80) return 'C';
      else if(m>=60 && m<70) return 'D';
      else return 'F';
    }
}
