#include <iostream>
#include <iomanip>
#include <sstream>
#include <chrono>

int main()
{
    // Create date string
    std::string date_str = "2022-03-17 10:45:30";
    // Create object to hold the date and time broken down into its components
    std::tm date_obj = {};
    // Create a istringstream object and initialize it with data_str
    std::istringstream ss(date_str);
    // Extract formatted data from the ss stream and store it in the date_obj variable. 
    ss >> std::get_time(&date_obj, "%Y-%m-%d %H:%M:%S");
    // Create a stringstream onject 
    std::stringstream formatted_date_ss;
    // Format the date_obj variable using the specified format %m/%d/%Y %H:%M:%S (month/day/year hour:minute:second) and write it to the formatted_date_ss stringstream.
    formatted_date_ss << std::put_time(&date_obj, "%m/%d/%Y %H:%M:%S");
    // Extracts the formatted date from the stringstream formatted_date_ss and converts it to a string
    std::string formatted_date = formatted_date_ss.str();

    // Print out the formatted date
    std::cout << formatted_date << std::endl;

    return 0;
}
