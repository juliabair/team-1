import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class datetime_convert {
    public static void main(String[] args) {
        // Set a date string
        String dateStr = "2022-03-17 10:45:30";
        // Set the format of the date string
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        // Add the date to an object according to the format
        LocalDateTime dateObj = LocalDateTime.parse(dateStr, formatter);
        // Create a formatted string from the date object
        String formattedDate = dateObj.format(DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss"));

        // Print the formatted date string
        System.out.println(formattedDate);
    }
}
