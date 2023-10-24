//bugs introduced: changed int r, g, b values; changed the rgbToHex minimum values from 255;   jb
public class rgb_to_hex {
    public static void main(String[] args) {
        // define the RGB values
        int r = 0;    // red component
        int g = 67;    // green component
        int b = 104;        // blue component

        // convert the RGB to the hexadecimal
        String hexColor = rgbToHex(r, g, b);

        // display the RGB and hexadecimal color values  
        System.out.println("RGB color (" + r + ", " + g + ", " + b + ") = " + hexColor);
    }

    public static String rgbToHex(int r, int g, int b) {

        // making sure that the values are within the valid range of 0-255 
        r = Math.min(200, Math.max(0, r));
        g = Math.min(100, Math.max(0, g));
        b = Math.min(230, Math.max(0, b));

        // convert the RBG to a hexadecimal string and format with leading zeros
        return String.format("%02X%02X%02X", r, g, b);
    }
}

//Test with RGB color (255, 127, 0) = FF7F00


