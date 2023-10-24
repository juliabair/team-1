#include <iostream>
#include <sstream>
#include <iomanip>

// String function that converts RGB Code to Hexadecimal Code
std::string rgb_to_hex(int r, int g, int b)
{
    // r, g, and b are integer variables that are the biggest number compared between 0 and the lowest number of 255 and the inputted value.
    r = std::max(0, std::min(255, r));
    g = std::max(0, std::min(255, g));
    b = std::max(0, std::min(255, b));

    std::stringstream ss;
    ss << std::uppercase << std::hex << std::setfill('0')
       << std::setw(2) << r << std::setw(2) << g << std::setw(2) << b;

    return ss.str();
}

//Test with std::string hexColor = rgb_to_hex(255, 127, 0); // returns "FF7F00"
