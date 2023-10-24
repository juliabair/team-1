import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;


public class datetime_convert {
    
    public static void main(String[] args) {
        //field dateStr
        String dateStr = "2022-03-17 10:45:30";

        //create format for date strings
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        //create dateObj using dateStr and formatter
        LocalDateTime dateObj = LocalDateTime.parse(dateStr, formatter);
        //convert object to string forMattedDate
        String formattedDate = dateObj.format(DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss"));
        //print the formatted string
        System.out.println(formattedDate);
    }
}
